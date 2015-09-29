from django.shortcuts import render
from votes.models import Vote, Ward
from votes.serializers import VoteSerializer, WardSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics



class VoteList(generics.ListCreateAPIView):
    """
    List all Votes, or create a new Vote
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a vote
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class WardList(generics.ListAPIView):
    """
    List all Wards
    """
    queryset = Ward.objects.all()
    serializer_class = WardSerializer





