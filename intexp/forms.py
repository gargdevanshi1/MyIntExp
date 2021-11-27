from django import forms
from django.contrib.auth.models import User
from intexp.models import RoundDetails, UserProfileInfo, Experience


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'width':'100%'}))
    class Meta:
        model = User
        fields = ('username' , 'email' , 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('Name' , 'DOB','Institution' , 'Qualification', 'YearOfPassing')


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('company' , 'job_profile','work_experience' )


class RoundForm(forms.ModelForm):
    class Meta:
        model = RoundDetails
        fields = (
            "duration",
            "about"
        )

class ApproveForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('isApproved',)