from rest_framework.serializers import ModelSerializer
from newsletters.serializers import NewsletterSerializer
from subscriptions.models import Subscriptions
from users.serializers import UsersSerializer


class SubscriptionSerializer(ModelSerializer):
    user = UsersSerializer()
    newsletter = NewsletterSerializer()

    class Meta:
        model = Subscriptions
        fields = '__all__'


class CreateSubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = '__all__'


class GetSubscriptionsUserSerializer(ModelSerializer):
    newsletter = NewsletterSerializer()

    class Meta:
        model = Subscriptions
        fields = '__all__'
