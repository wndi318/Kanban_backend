# Generated by Django 5.0.7 on 2024-08-01 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
