# Generated by Django 3.0.3 on 2020-04-02 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_useraddress_defalut'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='defalut',
        ),
    ]
