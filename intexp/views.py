from django.http import response
from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.urls import reverse
from django.views.generic.detail import DetailView
from intexp.forms import UserForm, ApproveForm
from intexp.models import RoundDetails, UserProfileInfo, Experience
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView,DetailView
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView

# Create your views here.

def main(request):
	return render(request,'main.html')

@csrf_protect
def login(request):
	if request.method=='POST':
		uname=request.POST.get('username')
		passw=request.POST.get('password')

		user=authenticate(username=uname,password=passw)
		if user:
			if user.is_active:
				auth_login(request,user)
				return HttpResponseRedirect(reverse('homepage'))
			else:
				return HttpResponse("User is inactive")
		else:
			messages.info(request, 'Sorry, wrong username or password. Please try again.')
			return render(request,'login.html',{'err':'Invalid User Credentials!'})

	else:
		return render(request,'login.html')

def registration(request):
	form_class = UserForm
	form = form_class(request.POST)
	if request.method == 'POST':
		form = UserForm(data=request.POST)
		if form.is_valid():
			user=form.save()
			user.set_password(user.password)
			user.save()
			name = request.POST.get('Name') 
			dob=request.POST.get('DOB')
			institution=request.POST.get('Institution')
			qualification=request.POST.get('Qualification')
			year_of_passing=request.POST.get('YearOfPassing')
			u=UserProfileInfo.objects.create(Name = name, DOB= dob, Institution=institution, Qualification=qualification, YearOfPassing = year_of_passing, user=user)
			u.user=user
			u.save()
			return HttpResponseRedirect(reverse('login'))
		else :
			messages.info(request, '\nSorry, this username already exists. Please try again with a different name.')
			return render(request,'register.html', {'user_form':form})
	return render(request,'register.html', {'user_form':form} )


def homepage (request) :
	return render (request, 'index.html')


@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))


def myprofile(request):
	active_user = UserProfileInfo.objects.filter(user = request.user)
	return render (request, 'profile.html', {'active_user' : active_user[0]})

exp_html = 'experiences.html'

@method_decorator(login_required, name='dispatch')
class my_experiences(ListView):
	model=Experience
	context_object_name='Experience'
	template_name=exp_html
	
	def get_queryset(self):
		return Experience.objects.filter(user = self.request.user)


def add_experience(request):
	if request.method=="POST":
		company = request.POST.get('company','')
		job_profile = request.POST.get('JobProfile','')
		work_experience = request.POST.get('workexp', '')
		rounds = []

		rounds.append(request.POST.get('duration1'))
		rounds.append(request.POST.get('desc1'))
		rounds.append(request.POST.get('duration2'))
		rounds.append(request.POST.get('desc2'))
		rounds.append(request.POST.get('duration3'))
		rounds.append(request.POST.get('desc3'))
		rounds.append(request.POST.get('duration4'))
		rounds.append(request.POST.get('desc4'))
		rounds.append(request.POST.get('duration5'))
		rounds.append(request.POST.get('desc5'))
		experience = Experience(user = request.user, company = company, job_profile = job_profile, work_experience = work_experience)
		experience.save()
		i=0
		while i<10 and rounds[i] != "":
			new_round = RoundDetails(duration= rounds[i], about = rounds[i+1], exp_id = experience)
			new_round.save()
			i+=2
		return HttpResponseRedirect(reverse('homepage'))
	return render(request, 'add_experience.html')

@method_decorator(login_required, name='dispatch')
class listofexperiences1(ListView):
	model=Experience
	context_object_name='Experience'
	template_name=exp_html
	
	def get_queryset(self):
		return Experience.objects.filter(job_profile = "Business Analyst").filter(isApproved= True)

@method_decorator(login_required, name='dispatch')
class listofexperiences2(ListView):
	model=Experience
	context_object_name='Experience'
	template_name=exp_html
	
	def get_queryset(self):
		return Experience.objects.filter(job_profile = "Data Analyst").filter(isApproved= True)

@method_decorator(login_required, name='dispatch')
class listofexperiences3(ListView):
	model=Experience
	context_object_name='Experience'
	template_name=exp_html
	
	def get_queryset(self):
		return Experience.objects.filter(job_profile = "Data Scientist").filter(isApproved= True)

@method_decorator(login_required, name='dispatch')
class listofexperiences4(ListView):
	model=Experience
	context_object_name='Experience'
	template_name=exp_html
	
	def get_queryset(self):
		return Experience.objects.filter(job_profile = "Marketing Manager").filter(isApproved= True)
	
@method_decorator(login_required, name='dispatch')
class listofexperiences5(ListView):
	model=Experience
	context_object_name='Experience'
	template_name=exp_html
	
	def get_queryset(self):
		return Experience.objects.filter(job_profile = "Operations Analyst").filter(isApproved= True)

@method_decorator(login_required, name='dispatch')
class listofexperiences6(ListView):
	model=Experience
	context_object_name='Experience'
	template_name=exp_html
	
	def get_queryset(self):
		return Experience.objects.filter(job_profile = "Software Developer").filter(isApproved= True)

@method_decorator(login_required, name='dispatch')
class listofexperiences7(ListView):
	model=Experience
	context_object_name='Experience'
	template_name=exp_html
	
	def get_queryset(self):
		return Experience.objects.filter(job_profile = "System Engineer").filter(isApproved= True)

@method_decorator(login_required, name='dispatch')
class ExperienceDetail(DetailView):
	model= Experience
	context_object_name='Experience_Detailing'
	template_name= 'detail.html'
	
	def get_context_data(self, **kwargs):
		context= super(ExperienceDetail,self).get_context_data(**kwargs)
		context['rounds'] = list(enumerate(RoundDetails.objects.filter(exp_id= self.object),1))
		return context


def login_moderator(request):
	if request.method=='POST':
		uname=request.POST.get('username')
		passw=request.POST.get('password')
		user=authenticate(username=uname,password=passw)
		if user and request.user.is_superuser:
			if user.is_active:
				#After authentication-> user will be true
				auth_login(request,user)
				return HttpResponseRedirect(reverse('moderator-homepage'))
			else:
				return HttpResponse("User is inactive")
		else:
			messages.info(request, 'Sorry, wrong username or password. Please try again.')
			return render(request,'moderator_login.html',{'err':'Invalid User Credentials!'})
	else:
		return render(request,'moderator_login.html')

class approve_experiences(ListView):
	model=Experience
	context_object_name='Experience'
	template_name='experiences_moderator.html'
	
	def get_queryset(self):
		return Experience.objects.filter(isApproved = False)


class ExperienceUpdateView(UpdateView):
	model = Experience
	context_object_name='Experience_Detailing'
	fields = [
		"isApproved"
	]
	template_name='detail_moderator.html'
	success_url = '../../../homepage/moderator'

	def get_context_data(self, **kwargs):
		context= super(ExperienceUpdateView,self).get_context_data(**kwargs)
		context['rounds'] = list(enumerate(RoundDetails.objects.filter(exp_id= self.object),1))
		return context