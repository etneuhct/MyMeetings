from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from minute.models import TaskAssignment, TopicConclusion, TopicDiscussion, Topic, MeetingParticipant, \
    Meeting, MeetingTask
from minute.resume import generate_pdf
from minute.serializers import TaskAssignmentSerializer, TopicConclusionSerializer, \
    TopicDiscussionSerializer, TopicSerializer, MeetingParticipantSerializer, MeetingSerializer, MeetingTaskSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    serializer_class = MeetingSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return Meeting.objects.filter(team__teammember__member=self.request.user)


class MeetingParticipantViewSet(viewsets.ModelViewSet):
    serializer_class = MeetingParticipantSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return MeetingParticipant.objects.filter(meeting__team__teammember__member=self.request.user)


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return Topic.objects.filter(meeting__team__teammember__member=self.request.user)


class TopicDiscussionViewSet(viewsets.ModelViewSet):
    serializer_class = TopicDiscussionSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return TopicDiscussion.objects.filter(topic__meeting__team__teammember__member=self.request.user)


class TopicConclusionViewSet(viewsets.ModelViewSet):
    serializer_class = TopicConclusionSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return TopicConclusion.objects.filter(topic__meeting__team__teammember__member=self.request.user)


class MeetingTaskViewSet(viewsets.ModelViewSet):
    serializer_class = MeetingTaskSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return MeetingTask.objects.filter(meeting__team__teammember__member=self.request.user)


class TaskAssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = TaskAssignmentSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return TaskAssignment.objects.filter(task__meeting__team__teammember__user=self.request.user)


class DownloadMinute(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        if not Meeting.objects.filter(team__teammember__member=self.request.user, pk=pk).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        pdf = generate_pdf(pk)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=Resume.pdf'
        return response
