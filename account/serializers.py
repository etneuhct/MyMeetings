from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from account.models import TeamMember, Team
from utils.mail import send_mail
from utils.password import create_random_password
import jinja2


UserModel = get_user_model()
username_validator = UnicodeUsernameValidator()


class TeamForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Team.objects.filter(teammember__member=self.context['request'].user)


def get_username_field():
    return serializers.CharField(
        max_length=50,
        required=True,
        validators=[username_validator, UniqueValidator(queryset=UserModel.objects.all(), lookup='iexact')])


def get_email_field():
    return serializers.EmailField(
        max_length=50,
        required=True,
        validators=[UniqueValidator(queryset=UserModel.objects.all(), lookup='iexact')])


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ["username", "first_name", "last_name", "id"]


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    email = get_email_field()
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)
    username = get_username_field()

    class Meta:
        model = UserModel
        fields = ["id", "username", "password", "email", "first_name", "last_name"]

    def create(self, validated_data):

        username = validated_data['username'].lower()
        email = validated_data['email'].lower() if "email" in validated_data else ''

        user = UserModel.objects.create(
            username=username,
            is_active=True,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=email
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class InvitationSerializer(serializers.ModelSerializer):

    username = get_username_field()
    email = get_email_field()

    class Meta:
        model = UserModel
        fields = ["id", "username", "email", "first_name", "last_name"]

    def create(self, validated_data):
        random_password = create_random_password()
        username = validated_data['username'].lower()
        email = validated_data['email'].lower() if "email" in validated_data else ''
        user = UserModel.objects.create(
            username=username,
            is_active=True,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=email
        )
        user.set_password(random_password)
        data = {
            "invited": UserSerializer(instance=user).data,
            'user': UserSerializer(instance=self.context['request'].user).data,
            'password': random_password
        }
        send_invitation_mail(data, user)
        return user


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['id', 'name']


class TeamMemberSerializer(serializers.ModelSerializer):

    team = TeamForeignKey()

    class Meta:
        model = TeamMember
        fields = ['id', 'team', 'member']


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ["username", "first_name", "last_name"]


class ChangePasswordSerializer(serializers.Serializer):
    model = UserModel
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


def send_invitation_mail(data, user):
    message = generate_invitation_message(data)
    send_mail(user.email, message_content=message, message_subject='Bienvenue !')


def generate_invitation_message(data):
    with open("templates/invitation.html", "r", encoding="utf-8") as invitation:
        invitation = jinja2.Template(invitation.read())
    return invitation.render(data)
