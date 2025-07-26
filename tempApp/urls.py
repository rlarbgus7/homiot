from django.urls import path
from tempApp import views

urlpatterns = [
    path('', views.index),
    path('input/', views.input),
    path('inputTwo/', views.inputow),
    path('spread/', views.inpujson),
    path('table/', views.test)
]
