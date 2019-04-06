from django import forms
from .models import NewsLetterUser

#Here, create a form, signup form and submit news

#form signup to use model form ==>NewsLetterUser
class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(required=True, label=' الايميل')
    class Meta:
        model = NewsLetterUser
        fields = ['email']
        #validte email
        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email



#form news but use Form only no model form
class NewsCreationForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


    
