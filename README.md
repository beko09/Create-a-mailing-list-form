# Create-a-mailing-list-form
A simple form for mailing lists messages via email


In this application we will do the following



go to settings.py add INSTALLED_APPS app like her

    INSTALLED_APPS = [
        'post.apps.PostConfig',
        ]
 and yuo need to add email settings  settings.py
 like these
 
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'xexample@gmail.com'
    EMAIL_HOST_PASSWORD = 'your passwoed'
    
    
 got to urls.py include post/urls.py
 
      path('', include('post.urls')),
      
      
 in app post create model in models.py
 
 
     class NewsLetterUser(models.Model):
        email = models.EmailField()
        date_added = models.DateTimeField(auto_now_add=True)

        def __str__(set):
            return set.email
            
in admin Register your models here.

    class NewsLetterAdmin(admin.ModelAdmin):
        list_display = ['email', 'date_added']
        search_fields = ['email']

    admin.site.register(NewsLetterUser,NewsLetterAdmin)

in form you nedd to creat some form

    class NewsletterForm(forms.ModelForm):
        email = forms.EmailField(required=True, label=' الايميل')
        class Meta:
            model = NewsLetterUser
            fields = ['email']
        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email

    class NewsCreationForm(forms.Form):
        subject = forms.CharField(max_length=100)
        message = forms.CharField(widget=forms.Textarea)
        
        
in vewis.py Add the functions in the file veiws.py in this repository 

        function newsletter_singup()
        function newsletter_unsubscribe()
        function control_newsletter()



in post/urls.py  add urls function
    
    urlpatterns = [
        path('newsletter_singup',newsletter_singup,name='newsletter_singup'),
        path('newsletter_unsubscribe',newsletter_unsubscribe,name='newsletter_unsubscribe'),
        path('control_newsletter',control_newsletter,name='control_newsletter'),

    ]

in  tamplate add all template in the file tamplate in this repository

        newsletter.html
        newsletter_unsubscribe.html
        control_newsletter.html
        
#Note
When you want to send new news to subscribers you have to go to the link page control_newsletter.html and then enter the title of the subject and write the message and just press the transmitter will be sent to all subscribers
    
    
Enjoy
