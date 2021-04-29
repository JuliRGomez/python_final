from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from users.serializers import UsersSerializer, CreateUsersAdminSerializer
from rest_framework.response import Response
from django.core.mail import send_mail


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny, )
        if self.request.method in ['GET', 'DELETE']:
            self.permission_classes = (IsAdminUser, )

        return super(UsersViewSet, self).get_permissions()


class UsersAdminView(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def get_permissions(self):
        self.permission_classes = (IsAdminUser,)
        return super(UsersAdminView, self).get_permissions()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'create':
            return CreateUsersAdminSerializer
        return UsersSerializer

    @action(methods=['POST'], detail=False)
    def invitation(self, request):
        email = request.data.get('email')
        if email:
            send_mail(
                'Admin Invitation',  # subject
                f'Please sing Up in the next URL:http://127.0.0.1:8000/register?token={request.auth} ',  # body
                'info@newsletter.com',  # from
                [email],  # to
                fail_silently=False,
            )
        return Response(
            status=status.HTTP_200_OK,
            data={"message": "Invitation sent"}
        )
