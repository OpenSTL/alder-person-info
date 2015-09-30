from django.test import TestCase
from .models import Vote, VotingRound, Ward, Bill

# Create your tests here.

class VotingRoundTestCase(TestCase):
    def setUp(self):
        bill = Bill(bill_number=123)
        bill.save()
        VotingRound(bill=bill).save()
        Ward(ward_number=5).save()

    def test_unique_wards(self):
        """ VotingRound contains at most 1 Vote for each Ward """
        votingRound = VotingRound.objects.get(bill__bill_number=123)
        ward5 = Ward.objects.get(ward_number=5)

        vote1 = Vote(ward=ward5, vote_decision="Aye")
        votingRound.add_vote(vote1)
        vote2 = Vote(ward=ward5, vote_decision="No")
        votingRound.add_vote(vote2)

        self.assertEqual(votingRound.vote_set.count(), 1)
        self.assertEqual(votingRound.vote_set.first().vote_decision, "No")

