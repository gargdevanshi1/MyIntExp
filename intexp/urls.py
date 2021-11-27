from django.contrib import admin
from django.urls import path
from . import views

# set urls for the app
urlpatterns = [
    path('', views.main,name='main'),
    path('login/student',views.login,name='login'),
    path('homepage/userlogout/',views.userlogout,name="userlogout"),
    path('registration/',views.registration,name='registration'),
    path('homepage/', views.homepage, name = 'homepage'),
    path('login/moderator/', views.login_moderator, name= 'login_moderator'),
    path('homepage/moderator', views.approve_experiences.as_view(), name = 'moderator-homepage'),
    path("experience/add/", views.add_experience, name="AddExperience"),
    path('business-analyst/', views.listofexperiences1.as_view(), name = 'listofexperiences1'),
    path('data-analyst/', views.listofexperiences2.as_view(), name = 'listofexperiences2'),
    path('data-scientist/', views.listofexperiences3.as_view(), name = 'listofexperiences3'),
    path('marketing-manager/', views.listofexperiences4.as_view(), name = 'listofexperiences4'),
    path('operations-analyst/', views.listofexperiences5.as_view(), name = 'listofexperiences5'),
    path('software-developer/', views.listofexperiences6.as_view(), name = 'listofexperiences6'),
    path('system-engineer/', views.listofexperiences7.as_view(), name = 'listofexperiences7'),
    path('experience/<int:pk>/',views.ExperienceDetail.as_view(),name='detail'),
    path('moderator/experience/<int:pk>/',views.ExperienceUpdateView.as_view(),name='detail-moderator'),
    path('myprofile/',views.myprofile,name="myprofile"),
    path("myexperiences/", views.my_experiences.as_view(), name="myexperiences"),
]