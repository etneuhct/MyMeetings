from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from account.models import TeamMember, Team
from account.serializers import RegistrationSerializer, TeamMemberSerializer, TeamSerializer, \
    UserSerializer, InvitationSerializer, UserUpdateSerializer, ChangePasswordSerializer

UserModel = get_user_model()


class RegisterView(CreateAPIView):

    model = UserModel
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer


class UserView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class InvitationView(CreateAPIView):

    model = UserModel
    permission_classes = [IsAuthenticated]
    serializer_class = InvitationSerializer


class EditUserView(UpdateAPIView):

    model = get_user_model()
    permissions = [IsAuthenticated]
    serializer_class = UserUpdateSerializer
    http_method_names = ['patch']

    def get_object(self):
        obj = self.request.user
        return obj


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = UserModel
    permission_classes = (IsAuthenticated,)
    http_method_names = ['put']

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return Team.objects.filter(teammember__member=self.request.user)

    def perform_create(self, serializer):
        team = serializer.save()
        TeamMember.objects.get_or_create(team=team, member=self.request.user)


class TeamMemberViewSet(viewsets.ModelViewSet):
    serializer_class = TeamMemberSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return TeamMember.objects.filter(team__teammember__member=self.request.user)
