# Generated by Django 3.1.1 on 2020-09-30 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('running', '0002_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='running',
            field=models.ManyToManyField(to='running.Running'),
        ),
    ]