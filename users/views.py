from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from users.serializers import UsersSerializer, CreateUsersAdminSerializer
from rest_framework.response import Response


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny, )
        return super(UsersViewSet, self).get_permissions()

    @action(methods=['POST', 'DELETE'], detail=False)
    def admin(self, request):
        print(request.user.is_staff)
        return Response(
            status=status.HTTP_200_OK,
            data='hola mundo'
        )


class UsersAdminView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUsersAdminSerializer
        return UsersSerializer
