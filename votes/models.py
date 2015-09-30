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
    An optional informal name for this bill
    """



class VotingRound(models.Model):
    """
    The record of a hearing in which aldermen voted to advance or impede
    the progress of a particular bill
    """

    date = models.DateField
    """
    The date on which this voting round took place
    """

    bill = models.ForeignKey(Bill)
    """
    The bill on which voters were deliberating in this voting round
    """

    def add_vote(self, vote):
        """  Add a new Vote instance to, or replace an old Vote instance in
        this VotingRound's vote_set. The vote_set represents the votes that were
        cast during this voting round.

        A VotingRound can have at most 1 Vote from each Ward. Therefore,
        vote will replace any Vote object already in self.vote_set whose ward
        is the same as vote.ward. """

        # delete any Votes in the vote_set whose ward is the same
        [ duplicate.delete() for duplicate
          in self.vote_set.filter(ward_id=vote.ward_id)]

        self.vote_set.add(vote)


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
        return 'Ward: %s | Vote: %s' % (self.ward.ward_number, self.vote_decision)

