# Generated by Django 2.0.13 on 2019-05-20 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190521_0322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='sidemenu',
            new_name='sidemenus',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='topping',
            new_name='toppings',
        ),
    ]