# Generated by Django 4.0 on 2022-06-10 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_remove_post_contents_opening'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='da content'),
            preserve_default=False,
        ),
    ]