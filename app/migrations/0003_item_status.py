# Generated by Django 3.2.5 on 2021-07-30 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_name_item_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(default='open', max_length=32),
        ),
    ]
