# Generated by Django 3.1.1 on 2020-09-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('running', '0003_users_running'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='running',
            field=models.ManyToManyField(blank=True, related_name='favorited', to='running.Running'),
        ),
    ]