from django.contrib.auth import get_user_model
from rest_framework import serializers

from minute.models import Topic, TaskAssignment, MeetingTask, Meeting
from minute.serializers import TopicDiscussionSerializer, TopicConclusionSerializer, MeetingParticipantSerializer

UserModel = get_user_model()


class TemplateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ["username", "first_name", "last_name", "id"]


class TemplateTopicSerializer(serializers.ModelSerializer):
    topicdiscussion_set = TopicDiscussionSerializer(many=True)
    topicconclusion_set = TopicConclusionSerializer(many=True)

    class Meta:
        model = Topic
        fields = ['id', 'meeting', 'topic', 'rank', 'topicdiscussion_set', 'topicconclusion_set']


class TemplateTaskAssignmentSerializer(serializers.ModelSerializer):

    user = TemplateUserSerializer()

    class Meta:
        model = TaskAssignment
        fields = ['id', 'task', 'user']


class TemplateTaskSerializer(serializers.ModelSerializer):

    taskassignment_set = TemplateTaskAssignmentSerializer(many=True)
    class Meta:
        model = MeetingTask
        fields = ['id', 'meeting', 'task', 'rank', 'taskassignment_set']


class TemplateMeetingSerializer(serializers.ModelSerializer):

    secretary = TemplateUserSerializer(many=False)
    meetingparticipant_set = MeetingParticipantSerializer(many=True)
    topic_set = TemplateTopicSerializer(many=True)
    meetingtask_set = TemplateTaskSerializer(many=True)

    class Meta:
        model = Meeting
        fields = [
            'id', 'name', 'purpose', 'date', 'team', 'start_date', 'meetingtask_set',
            'end_date', 'secretary', 'meetingparticipant_set', 'topic_set'
        ]
