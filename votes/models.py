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




VOTE_CHOICES = [
    'Aye',
    'No',
    'Present',
    'Did not vote',
]

class Vote(models.Model):
    """
    The record of a vote that was cast by an alderman regarding a particular bill
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

    def __str__(self):
        return 'Ward: %s | Wote: %s' % (self.ward_number, self.vote_decision)

