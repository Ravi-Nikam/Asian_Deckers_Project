# Generated by Django 3.0.3 on 2020-04-02 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_remove_useraddress_defalut'),
    ]

    operations = [
        migrations.CreateModel(
            name='paytm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='ABC', max_length=120, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, default=10.99, max_digits=1000)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterModelOptions(
            name='useraddress',
            options={'ordering': ['-updated', '-timestamp']},
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='amount',
        ),
    ]
