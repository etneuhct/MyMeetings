"""meeting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView

from account.views import RegisterView, TeamMemberViewSet, TeamViewSet, UserView, InvitationView, \
    EditUserView, ChangePasswordView
from minute.views import TaskAssignmentViewSet, TopicConclusionViewSet, TopicDiscussionViewSet, \
    TopicViewSet, MeetingParticipantViewSet, MeetingViewSet, MeetingTaskViewSet, DownloadMinute
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Meeting API")

router = DefaultRouter()

router.register(r'meeting', MeetingViewSet, basename='meeting')
router.register(r'meeting-participant', MeetingParticipantViewSet, basename='meeting_participant')
router.register(r'topic', TopicViewSet, basename='topic')
router.register(r'topic-discussion', TopicDiscussionViewSet, basename='topic_discussion')
router.register(r'topic-conclusion', TopicConclusionViewSet, basename='topic_conclusion')
router.register(r'task', MeetingTaskViewSet, basename='meeting_task')
router.register(r'task-assignment', TaskAssignmentViewSet, basename='task_assignment')
router.register(r'team', TeamViewSet, basename='team')
router.register(r'team-member', TeamMemberViewSet, basename='team_member')

urlpatterns = [
    path("v1/", include(router.urls)),
    path('v1/user/login/', TokenObtainPairView.as_view(), name='user_login'),
    path('v1/user/registration/', RegisterView.as_view(), name='user_registration'),
    path('v1/user/invitation/', InvitationView.as_view(), name='user-invitation'),
    path('v1/user/edit/', EditUserView.as_view(), name='user_edit'),
    path('v1/user/change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('v1/user/list/', UserView.as_view(), name='user_list'),
    url('v1/download/minute/(?P<pk>\d+)$', DownloadMinute.as_view(), name='download_minute'),
]

"""path('api/login/', LoginView.as_view(), name='login'),
path('api/registration/', RegisterView.as_view(), name='registration'),
path('api/users/', UserView.as_view(), name='users'),"""

"""
    path('admin/', admin.site.urls),
    path('openapi', get_schema_view(
            title="Meeting",
            description="My meeting Api",
            version="1.0.0",
            permission_classes=[AllowAny]
        ), name='openapi-schema'),
"""
