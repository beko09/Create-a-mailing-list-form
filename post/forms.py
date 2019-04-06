from django import forms
from .models import NewsLetterUser


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


    