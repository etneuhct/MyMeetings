# Generated by Django 3.1.2 on 2020-10-24 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userteam')),
            ],
        ),
        migrations.CreateModel(
            name='Minute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minute.meeting')),
                ('secretary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MinuteTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('minute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minute.minute')),
            ],
        ),
        migrations.CreateModel(
            name='TopicTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=500)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minute.minutetopic')),
            ],
        ),
        migrations.CreateModel(
            name='TopicDiscussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discussion', models.CharField(max_length=500)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minute.minutetopic')),
            ],
        ),
        migrations.CreateModel(
            name='TopicConclusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conclusion', models.CharField(max_length=500)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minute.minutetopic')),
            ],
        ),
        migrations.CreateModel(
            name='TaskAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minute.topictask')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present', models.BooleanField(default=False)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minute.meeting')),
            ],
        ),
    ]
