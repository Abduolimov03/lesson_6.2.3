from django.urls import path
from .views import home_page, home, mobile, mebel

urlpatterns = [
    path('home_page/', home_page, name='home_page'),
    path('home/', home, name='home'),
    path('mobile/', mobile, name='mobile'),
    path('mebel/', mebel, name='mebel')
]