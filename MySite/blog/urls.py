from django.urls import path  
from . import views

urlpatterns = [  
    path('', views.home),  
    path('blog/contacts/', views.contacts, name='blog-contacts'),
]
