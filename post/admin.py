from django.contrib import admin
from .models import NewsLetterUser


# Register your models here.


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_added']
    search_fields = ['email']

    

admin.site.register(NewsLetterUser,NewsLetterAdmin)


