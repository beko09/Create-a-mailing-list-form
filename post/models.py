from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
  


    
# Create your models here.






class NewsLetterUser(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(set):
        return set.email


