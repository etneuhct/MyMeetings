# Generated by Django 3.1.2 on 2020-10-25 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minute', '0003_auto_20201025_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='topicconclusion',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='topicdiscussion',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='topictask',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]