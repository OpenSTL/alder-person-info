from django.shortcuts import render
from votes.models import Vote
from votes.serializers import VoteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class VoteList(APIView):
    """
    List all Votes, or create a new Vote
    """
    def get(self, request, format=None):
        votes = Vote.objects.all()
        serializer = VoteSerializer(votes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoteDetail(APIView):
    """
    Retrieve, update or delete a vote
    """



