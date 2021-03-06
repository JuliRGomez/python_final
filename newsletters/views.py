from rest_framework import status, request
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from newsletters.models import Newsletters
from newsletters.serializers import CreateNewsletterSerializer, NewsletterSerializer


class NewsletterViewSet(ModelViewSet):
    queryset = Newsletters.objects.all()
    serializer_class = CreateNewsletterSerializer

    def get_permissions(self):
        self.permission_classes = (IsAdminUser, )
        return super(NewsletterViewSet, self).get_permissions()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'create':
            return CreateNewsletterSerializer

        return NewsletterSerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tags')
        if tag:
            data = self.queryset.filter(tags__name=tag)  # __icontains
            return data
        return self.queryset

    @action(methods=['POST'], detail=False)
    def member(self, request):
        newsletter = request.data.get('newsletter')
        members = request.data.get('members')
        newsletter_to_update = Newsletters.objects.get(id=newsletter)
        for element in members:
            newsletter_to_update.members.add(element)
        newsletter_to_update.save()
        serialized = NewsletterSerializer(newsletter_to_update)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )

    @action(methods=['GET'], detail=False)
    def owns(self, request):
        id_user = request.user.id
        newsletters = Newsletters.objects.filter(user_id=id_user)
        serialized = NewsletterSerializer(newsletters, many=True)
        return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )


