from rest_framework.viewsets import ModelViewSet

from tags.models import Tags
from tags.serializers import CreateTagSerializer


class TagsViewSet(ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = CreateTagSerializer
