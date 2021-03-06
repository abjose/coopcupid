# Generated by Django 4.0 on 2022-05-31 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_alter_membership_member_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='contents',
        ),
        migrations.CreateModel(
            name='Opening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(verbose_name='date created')),
                ('is_active', models.BooleanField(default=False)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.community')),
            ],
        ),
    ]
