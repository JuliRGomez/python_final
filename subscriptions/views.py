from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from newsletters.models import Newsletters
from subscriptions.models import Subscriptions
from subscriptions.serializers import SubscriptionSerializer, CreateSubscriptionSerializer, \
    GetSubscriptionsUserSerializer
from rest_framework.response import Response


class SubscriptionViewSet(ModelViewSet):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionSerializer

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'create':
            return CreateSubscriptionSerializer
        return SubscriptionSerializer

    def create(self, request):
        id_user = request.user.id
        id_newsletter = request.data.get('newsletter')
        request_data = {'user': id_user, 'newsletter': id_newsletter}
        serialized = CreateSubscriptionSerializer(data=request_data)
        subscription = Subscriptions.objects.filter(user_id=id_user, newsletter=id_newsletter)
        newsletter_to_subscribe = Newsletters.objects.get(id=id_newsletter)
        target = newsletter_to_subscribe.target
        votes = newsletter_to_subscribe.votes
        if votes == target:
            if not subscription:
                if not serialized.is_valid():
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST,
                        data=serialized.errors
                    )
                serialized.save()
                return Response(
                    status=status.HTTP_200_OK,
                    data=serialized.data
                )
            else:
                return Response(
                    status=status.HTTP_200_OK,
                    data={"message": "already subscribed"}
                )
        else:
            return Response(
                status=status.HTTP_200_OK,
                data={"message": "not enough votes"}
            )

    def destroy(self, request, pk=None):
        id_user = request.user.id
        newsletter = self.get_object()
        serialized = SubscriptionSerializer(newsletter)
        if serialized.data.get('user').get('id') == id_user:
            newsletter.delete()
            return Response(
                status=status.HTTP_200_OK,
                data={"message": "subscription finished"}
            )
        else:
            return Response(
                status=status.HTTP_401_UNAUTHORIZED,
                data={"message": "unauthorized"}
            )

    @action(methods=['GET'], detail=False, permission_classes=[IsAdminUser])
    def user(self, request, pk=None):
        id_user = request.user.id
        data = Subscriptions.objects.filter(user_id=id_user)
        serialized = GetSubscriptionsUserSerializer(data, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
            )

