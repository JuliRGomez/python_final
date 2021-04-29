from rest_framework.serializers import ModelSerializer
from newsletters.models import Newsletters


class NewletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletters
        fields = ('name', 'description', 'image', 'votes', 'target', 'tags')


class CreateNewletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletters
        fields = '__all__'
