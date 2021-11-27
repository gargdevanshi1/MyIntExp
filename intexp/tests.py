from django.test import TestCase
from .models import Experience, RoundDetails, UserProfileInfo, User
# Create your tests here.

class BasicTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username ="test case1", password ="testing")
        self.userinfo = UserProfileInfo.objects.create(user = self.user, Name ="Test Case", DOB= '1990-01-01', Institution='Name of University', Qualification='Degree', YearOfPassing = 2100)
        self.exp = Experience.objects.create(user= self.user, company= 'Name of organization', job_profile='Job Role', work_experience='>4 years', isApproved = False)
        self.round = RoundDetails.objects.create(exp_id = self.exp,duration = 100, about = "This is a test case to test \n the fields of the round model")

    def test_fields_user(self):
        record_user = User.objects.get(pk=self.user.id)
        self.assertEqual(record_user,self.user)

    def test_fields_user_info(self):
        record_user_info = UserProfileInfo.objects.get(pk= self.userinfo.id)
        self.assertEqual(record_user_info, self.userinfo)
        
    def test_fields_exp(self):
        record_exp = Experience.objects.get(pk=self.exp.exp_id)
        self.assertEqual(record_exp,self.exp)

    def test_fields_round(self):
        record_round = RoundDetails.objects.get(pk = self.round.r_id)
        self.assertEqual(record_round,self.round)

