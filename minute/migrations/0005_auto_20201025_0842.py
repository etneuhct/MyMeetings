# Generated by Django 3.1.2 on 2020-10-25 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minute', '0004_auto_20201025_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=500)),
                ('rank', models.IntegerField(default=0)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minute.meeting')),
            ],
        ),
        migrations.AlterField(
            model_name='taskassignment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minute.meetingtask'),
        ),
    ]
