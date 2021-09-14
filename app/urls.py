from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('signup', views.user_signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('get_question <str:sub>', views.get_question, name='get_question'),
    path('check', views.check_answer, name='check'),
    path('next', views.next_question, name='next'),
    path('result', views.result, name='result')
]
