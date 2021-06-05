from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('office/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('favorite/', views.favorite, name='favorite'),
    path('coming/', views.coming, name='coming'),
    path('register/', views.register, name='register'),
    path('add_favorite', views.add_favorite, name='add_favorite'),
    path('match/<str:slug>/', views.match_details, name='match_details'),
    path('buying/<str:slug>/', views.buying_ticket, name='buying_ticket'),
    path('my_fav/<str:name>/', views.my_fav, name='my_fav'),
    path('confirm/<str:slug>/', views.confirm, name='confirm'),
    path('check/<str:title>/', views.check, name='check'),
    path('return/', views.return_ticket, name='return'),
]
