# Generated by Django 3.2.4 on 2021-07-03 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0018_auto_20210629_1032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={'ordering': ['-id']},
        ),
    ]