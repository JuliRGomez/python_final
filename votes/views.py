from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from newsletters.models import Newsletters
from votes.models import Votes
from votes.serializers import VoteSerializer
from rest_framework.response import Response


class VotesViewSet(ModelViewSet):
    queryset = Votes.objects.all()
    serializer_class = VoteSerializer

    def create(self, request):
        id_user = request.user.id
        id_newsletter = request.data.get('newsletter')
        vote = Votes.objects.filter(user_id=id_user, newsletter=id_newsletter)
        if vote:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": "only one vote by user"}
            )
        else:
            request_data = {'user': id_user, 'newsletter': id_newsletter}
            serialized = VoteSerializer(data=request_data)
            if not serialized.is_valid():
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data=serialized.errors
                )
            serialized.save()
            newsletter_to_vote = Newsletters.objects.get(id=id_newsletter)
            newsletter_to_vote.votes = newsletter_to_vote.votes + 1
            newsletter_to_vote.save()
            return Response(
                status=status.HTTP_201_CREATED,
                data=serialized.data
            )

    def delete(self, request, pk=None):
        id_user = request.user.id
        vote = self.get_object()
        serialized = VoteSerializer(vote)
        if serialized.data.get('user').get('id') == id_user:
            vote.delete()
            newsletter_to_vote = Newsletters.objects.get(id=serialized.data.get('id'))
            newsletter_to_vote.votes = newsletter_to_vote.votes - 1
            newsletter_to_vote.save()
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                status=status.HTTP_401_UNAUTHORIZED,
                data={"message": "unauthorized"}
            )
