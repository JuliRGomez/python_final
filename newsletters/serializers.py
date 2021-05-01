from rest_framework.serializers import ModelSerializer
from newsletters.models import Newsletters


class NewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletters
        fields = ('id', 'name', 'description', 'image', 'votes', 'target', 'tags','members')


class CreateNewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletters
        fields = '__all__'
