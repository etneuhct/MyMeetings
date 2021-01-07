from django.contrib.auth.models import User
from django.db import models


class Meeting(models.Model):
    name = models.CharField(max_length=100)
    purpose = models.TextField()
    date = models.DateTimeField()
    team = models.ForeignKey("account.Team", on_delete=models.CASCADE)
    place = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    secretary = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="secretary")
    organizer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="organizer")


class MeetingParticipant(models.Model):
    meeting = models.ForeignKey("meeting", on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    present = models.BooleanField(default=False)

    class Meta:
        unique_together = [("meeting", "guest")]


class Topic(models.Model):
    meeting = models.ForeignKey("Meeting", on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    rank = models.IntegerField(default=0)


class TopicDiscussion(models.Model):
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE)
    discussion = models.TextField()
    rank = models.IntegerField(default=0)


class TopicConclusion(models.Model):
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE)
    conclusion = models.TextField()
    rank = models.IntegerField(default=0)


class TaskAssignment(models.Model):
    task = models.ForeignKey("MeetingTask", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = [("task", "user")]


class MeetingTask(models.Model):
    meeting = models.ForeignKey("Meeting", on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    rank = models.IntegerField(default=0)
    dead_line = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    details = models.TextField(blank=True, null=True)
