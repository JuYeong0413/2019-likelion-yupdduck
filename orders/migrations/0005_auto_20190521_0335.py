# Generated by Django 2.0.13 on 2019-05-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190521_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='drink',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]