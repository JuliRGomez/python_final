from rest_framework.viewsets import ModelViewSet
from tags.models import Tags
from tags.serializers import CreateTagSerializer, TagSerializer


class TagsViewSet(ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'create':
            return CreateTagSerializer
        return TagSerializer
