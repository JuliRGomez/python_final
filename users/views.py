from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from users.serializers import UsersSerializer, CreateUsersAdminSerializer, CreateUsersSerializer
from rest_framework.response import Response
from django.core.mail import send_mail
from newsletters_api.celery import app


@app.task(name='send_email_invitation')
def send_email_invitation(email, token):
    send_mail(
        'Admin Invitation',  # subject
        f'Please sing Up in the next URL:http://127.0.0.1:8000/register?token={token} ',  # body
        'info@newsletter.com',  # from
        [email],  # to
        fail_silently=False,
    )


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'create':
            return CreateUsersSerializer
        return UsersSerializer

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
        token = str(request.auth)
        if email:
            send_email_invitation.apply_async(args=[email, token])
            return Response(
                status=status.HTTP_200_OK,
                data={"message": "Invitation sent"}
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={"message": "email is required"}
        )

