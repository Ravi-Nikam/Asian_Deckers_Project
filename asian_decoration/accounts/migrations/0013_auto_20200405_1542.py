# Generated by Django 3.0.3 on 2020-04-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200403_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='End_date',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraddress',
            name='Str_date',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]