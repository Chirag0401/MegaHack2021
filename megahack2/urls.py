from django.urls import path
from .views import index, team, register
urlpatterns = [
    path('',index,name="index"),
    path('register/',register,name="register"),
     path('team/',team,name="team"),
]
