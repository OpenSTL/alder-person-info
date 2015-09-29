from django.db import models


VOTE_CHOICES = [
    'Aye',
    'No',
    'Present',
    'Did not vote',
]

class Vote(models.Model):
    """
    The record of a vote that was cast by an Alderman regarding a particular Bill
    """


    # owner = models.ForeignKey('auth.User', related_name='snippets')


    ward_number = models.CharField(default="0", max_length=100)
    """
    The city ward number of the ward whose alderman cast this vote
    """

    vote_decision = models.CharField(default="Did not vote", max_length=100)
    """
    The stance that the voter took regarding the bill. Choices are:
        'Aye':          in favor of the bill
        'No':           against the bill
        'Present':      undecided or abstaining from voting
        'Did not vote': was not attend the meeting
    """

class Ward(models.Model):
    """
    A geographical district of the city whose residents elect an alderman
    """
    ward_number = models.CharField(default="0", max_length=100)
    """
    The official number by which this ward is designated
    """