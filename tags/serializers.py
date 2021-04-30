from rest_framework.serializers import ModelSerializer
from tags.models import Tags


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class CreateTagSerializer(ModelSerializer):
    class Meta:
        model = Tags
        fields = ('name', 'slug')
