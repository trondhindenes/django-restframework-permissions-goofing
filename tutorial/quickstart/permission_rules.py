import rules
from django.contrib.auth.models import User

from quickstart.models import Task


@rules.predicate
def is_task_reported_by(user: User, task: Task):
    return task.reported_by == user


@rules.predicate
def is_member_of_task_group_owning_task(user: User, task: Task):
    # preload related objects by using select_related, this keeps the number of queries down
    task = Task.objects.select_related("task_group").select_related("task_group__owned_by_group").get(id=task.id)
    if user.groups.filter(name=task.task_group.owned_by_group).exists():
        return True
    return False


# The "can_change_task" is true when either the user is the reported_by user,
# or the task's task group matches a group the user is a member of
can_change_task = is_task_reported_by | is_member_of_task_group_owning_task

rules.add_perm(
    "quickstart.change_task", can_change_task
)
