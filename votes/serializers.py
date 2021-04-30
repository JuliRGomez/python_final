from rest_framework.serializers import ModelSerializer

from votes.models import Votes


class VoteSerializer(ModelSerializer):
    class Meta:
        model = Votes
        fields = '__all__'
