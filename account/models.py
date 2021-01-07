from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100)


class TeamMember(models.Model):
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("team", "member"), )
