# Generated by Django 5.0.7 on 2024-08-06 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_remove_task_assigned_to_task_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('todo', 'Todo'), ('inProgress', 'In Progress'), ('awaitFeedback', 'Await Feedback'), ('done', 'Done')], default='todo', max_length=15),
        ),
    ]
