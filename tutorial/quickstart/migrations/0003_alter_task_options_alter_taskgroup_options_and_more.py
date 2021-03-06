# Generated by Django 4.0.5 on 2022-06-18 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("quickstart", "0002_alter_taskgroup_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={},
        ),
        migrations.AlterModelOptions(
            name="taskgroup",
            options={},
        ),
        migrations.AddField(
            model_name="taskgroup",
            name="owned_by_group",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="auth.group"
            ),
            preserve_default=False,
        ),
    ]
