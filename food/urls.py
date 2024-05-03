from django.urls import path
from food.views import contact
from . import views
urlpatterns = [
    path('', views.home),
    path('user/',views.User,name='User'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path("users/",views.Users,name='Users')
]