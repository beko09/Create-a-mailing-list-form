# Create-a-mailing-list-form
A simple form for mailing lists messages via email
In this application we will do the following
go to settings add INSTALLED_APPS app like her
    INSTALLED_APPS = [

        'post.apps.PostConfig',
        ]
 got to urls.py include post/urls.py
 
      path('', include('post.urls')),
      
      
 in app post create model in models.py
 
 
     class NewsLetterUser(models.Model):
        email = models.EmailField()
        date_added = models.DateTimeField(auto_now_add=True)

        def __str__(set):
            return set.email
in vewis.py Add the functions in the file veiws.py in this repository 


in post/urls.py  add urls function

in  tamplate add all template in the file tamplate in this repository
 
    
    