from rest_framework.viewsets import ModelViewSet

from votes.models import Votes
from votes.serializers import VoteSerializer


class VotesViewSet(ModelViewSet):
    queryset = Votes.objects.all()
    serializer_class = VoteSerializer
