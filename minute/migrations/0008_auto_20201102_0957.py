# Generated by Django 3.1.2 on 2020-11-02 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('minute', '0007_auto_20201101_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='organizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organizer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meeting',
            name='place',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='meetingtask',
            name='dead_line',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meetingtask',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meetingtask',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='purpose',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='secretary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='secretary', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meetingtask',
            name='task',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='topicconclusion',
            name='conclusion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='topicdiscussion',
            name='discussion',
            field=models.TextField(),
        ),
        migrations.AlterUniqueTogether(
            name='meetingparticipant',
            unique_together={('meeting', 'guest')},
        ),
        migrations.AlterUniqueTogether(
            name='taskassignment',
            unique_together={('task', 'user')},
        ),
    ]
