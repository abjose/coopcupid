# Generated by Django 4.0 on 2022-05-27 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_remove_membership_membership_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='member_type',
            field=models.IntegerField(choices=[(1, 'Full'), (2, 'Social'), (3, 'Alum'), (4, 'Follower')]),
        ),
    ]
