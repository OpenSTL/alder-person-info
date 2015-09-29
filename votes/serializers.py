from rest_framework import serializers
from votes.models import Vote, Ward

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('ward', 'vote_decision',)


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ('ward_number',)