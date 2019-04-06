from django.urls import path
from .views import (newsletter_singup,newsletter_unsubscribe,control_newsletter,search)


urlpatterns = [
    path('newsletter_singup',newsletter_singup,name='newsletter_singup'),
    path('newsletter_unsubscribe',newsletter_unsubscribe,name='newsletter_unsubscribe'),
    path('control_newsletter',control_newsletter,name='control_newsletter'),
  
    
  
]