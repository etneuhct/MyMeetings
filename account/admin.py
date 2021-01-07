from django.contrib import admin

# Register your models here.
from account.models import TeamMember, Team

admin.site.register(Team)
admin.site.register(TeamMember)
