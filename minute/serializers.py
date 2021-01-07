from rest_framework import serializers
from account.serializers import UserSerializer, TeamForeignKey
from minute.models import TaskAssignment, TopicConclusion, TopicDiscussion, Topic, MeetingParticipant, \
    Meeting, MeetingTask


class MeetingForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Meeting.objects.filter(team__teammember__member=self.context['request'].user)


class TopicForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Topic.objects.filter(meeting__team__teammember__member=self.context['request'].user)


class MeetingTaskForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return MeetingTask.objects.filter(meeting__team__teammember__member=self.context['request'].user)


class MeetingSerializer(serializers.ModelSerializer):

    team = TeamForeignKey()

    class Meta:
        model = Meeting
        fields = ['id', 'name', 'purpose', 'date', 'team', 'start_date', 'end_date', 'secretary', 'place']


class MeetingParticipantSerializer(serializers.ModelSerializer):

    meeting = MeetingForeignKey()

    class Meta:
        model = MeetingParticipant
        fields = ['id', 'meeting', 'guest', 'present']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['guest'] = UserSerializer(instance=instance.guest).data
        return data


class TopicSerializer(serializers.ModelSerializer):

    meeting = MeetingForeignKey()

    class Meta:
        model = Topic
        fields = ['id', 'meeting', 'topic', 'rank']


class TopicDiscussionSerializer(serializers.ModelSerializer):

    topic = TopicForeignKey()

    class Meta:
        model = TopicDiscussion
        fields = ['id', 'topic', 'discussion', 'rank']


class TopicConclusionSerializer(serializers.ModelSerializer):

    topic = TopicForeignKey()

    class Meta:
        model = TopicConclusion
        fields = ['id', 'topic', 'conclusion', 'rank']


class MeetingTaskSerializer(serializers.ModelSerializer):

    meeting = MeetingForeignKey()

    class Meta:
        model = MeetingTask
        fields = ['id', 'meeting', 'task', 'rank']


class TaskAssignmentSerializer(serializers.ModelSerializer):

    task = MeetingTaskForeignKey()

    class Meta:
        model = TaskAssignment
        fields = ['id', 'task', 'user']
