import sys

from django.conf import settings
from django.contrib.auth.models import User, Group
from django.db import connection
from django.template import Template, Context
from django.test import TestCase

from quickstart.models import TaskGroup, Task
from quickstart import permission_rules


class TaskTest(TestCase):
    def setUp(self):
        from django.conf import settings
        settings.DEBUG = True

    def tearDown(self):
        from django.db import connection
        for query in connection.queries:
            print(f"{query['sql']}\n")

    def test_direct_permissions(self):
        group1 = Group.objects.create(name="group1")
        user1 = User.objects.create(username="user1")
        task_group1 = TaskGroup.objects.create(name="group1", owned_by_group=group1)
        task1 = Task.objects.create(
            summary="what", content="what", task_group=task_group1, reported_by=user1
        )
        self.assertTrue(user1.has_perm("quickstart.change_task", task1))

    def test_direct_group_permissions(self):
        group1 = Group.objects.create(name="group1")
        user1 = User.objects.create(username="user1")
        user1.groups.add(group1)
        task_group1 = TaskGroup.objects.create(name="group1", owned_by_group=group1)
        task1 = Task.objects.create(
            summary="what", content="what", task_group=task_group1, reported_by=user1
        )
        self.assertTrue(user1.has_perm("quickstart.change_task", task1))

    # noinspection DuplicatedCode
    def test_indirect_group_permissions(self):
        group1 = Group.objects.create(name="group1")
        user1 = User.objects.create(username="user1")

        user1.groups.add(group1)

        user2 = User.objects.create(username="user2")
        user2.groups.add(group1)

        task_group1 = TaskGroup.objects.create(name="group1", owned_by_group=group1)
        task1 = Task.objects.create(
            summary="what", content="what", task_group=task_group1, reported_by=user1
        )

        # user2 has access to the task via the task group/group
        self.assertTrue(user2.has_perm("quickstart.change_task", task1))

    def test_indirect_group_permissions_noaccess(self):
        group1 = Group.objects.create(name="group1")
        group2 = Group.objects.create(name="group2")
        user1 = User.objects.create(username="user1")

        user1.groups.add(group1)

        user2 = User.objects.create(username="user2")
        user2.groups.add(group2)

        task_group1 = TaskGroup.objects.create(name="group1", owned_by_group=group1)
        task1 = Task.objects.create(
            summary="what", content="what", task_group=task_group1, reported_by=user1
        )

        # User2 does not have access thru group2
        self.assertFalse(user2.has_perm("quickstart.change_task", task1))
