# Generated by Django 2.2.2 on 2019-07-05 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_auto_20190705_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
    ]