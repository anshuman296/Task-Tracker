# Generated by Django 4.0.4 on 2022-04-20 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_team_user_team_team_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('priority', models.BooleanField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('assigned', models.BooleanField()),
                ('in_progress', models.BooleanField()),
                ('under_review', models.BooleanField()),
                ('done', models.BooleanField()),
                ('team_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
