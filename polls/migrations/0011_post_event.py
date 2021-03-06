# Generated by Django 4.0 on 2022-05-17 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_question_question_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(verbose_name='date created')),
                ('contents', models.TextField()),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.community')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('description', models.TextField()),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.community')),
            ],
        ),
    ]
