from rest_framework import status, request
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from newsletters.models import Newsletters
from newsletters.serializers import CreateNewletterSerializer, NewletterSerializer
from tags.serializers import TagSerializer


class NewsletterViewSet(ModelViewSet):
    queryset = Newsletters.objects.all()
    serializer_class = CreateNewletterSerializer

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'create':
            return CreateNewletterSerializer

        return NewletterSerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tags')
        if tag:
            datos = self.queryset.filter(tag__icontains=tag)
            return datos
        return self.queryset

    """
    if request.method == 'POST':
        users_id = request.data['users']
        for user_id in users_id:
            user = User.objects.get(id=user_id)
            Newsletters.users.add(user)
        return Response(
            status=status.HTTP_200_OK
        )
"""