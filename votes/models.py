from django.db import models



class Ward(models.Model):
    """
    A district of the city whose residents elect and are represented by an alderman
    """

    ward_number = models.CharField(default="0", max_length=100,)
    """
    The official number used to designate this ward
    """

    readonly_fields = ('ward_number', )

    def __str__(self):
        return 'Ward %s' % self.ward_number


class Bill(models.Model):
    """
    A piece of legislation that has been and/or will be voted on by the city aldermen
    """

    bill_number = models.CharField(max_length=100)
    """
    The official number used in city legislation to designate this bill
    """

    title = models.CharField(blank=True, max_length=100)
    """
    An informal name for this bill
    """



class VotingRound(models.Model):
    """
    The record of a hearing on a particular bill in which each alderman voted
    """

    date = models.DateField
    """
    The date on which the voting round took place
    """

    bill = models.ForeignKey(Bill)
    """
    The bill that this voting round is deciding on
    """


# TODO turn this into an enum

VOTE_CHOICES = [
    'Aye',
    'No',
    'Present',
    'Did not vote',
]

class Vote(models.Model):
    """
    The record of a vote that was cast by an alderman during a particular
    voting round of a particular bill
    """

    ward = models.ForeignKey(Ward, default=0)
    """
    The ward whose alderman cast this vote
    """

    vote_decision = models.CharField(default="Did not vote", max_length=100)
    """
    The stance that the voter took regarding the bill. Choices are:
        'Aye':          in favor of the bill
        'No':           against the bill
        'Present':      undecided or abstained from voting
        'Did not vote': was not in attendance at the meeting
    """

    voting_round = models.ForeignKey(VotingRound, default=0)
    """
    The voting round in which this vote took place
    """

    def __str__(self):
        return 'Ward: %s | Wote: %s' % (self.ward.ward_number, self.vote_decision)

