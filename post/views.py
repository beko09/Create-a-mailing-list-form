from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404,Http404
from django.contrib import messages
from .models import NewsLetterUser
from django.http import HttpResponse
from .forms import ,NewsletterForm,NewsCreationForm
from django.conf import settings
from django.core.mail import send_mail, get_connection,BadHeaderError,EmailMultiAlternatives




#In this function the user will log in and send him a thank you messagein this function user rgister and send email

def newsletter_singup(request):
    form = NewsletterForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        #Here I am sure that the email is registered or not
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            #if email register show  messages warning
            messages.warning(request,f'هذا الايميل مشترك مسبقا')
        else:
            # if email not register save this email and show messages success
            instance.save()
            messages.success(request,f'تم الاشتراك بنجاح ')
            #l am use function send() to send email
            subject = " الاشتراك البريدي"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            #Here you can use an external text file so that you type what you want
            # with open(settings.BASE_DIR + "/templates/sign_up_email.txt") as f:
            #     signup_message = f.read()
            # lam use simle text
            signup_message = """ helo wel come """
            message = EmailMultiAlternatives(subject=subject,body=signup_message,from_email=from_email,to=to_email)
            html_template = get_template("sign_up_email.html").render()
            message.attach_alternative(html_template,"text/html")
            message.send()
    context ={
        'form': form
    }   
    return render(request,'newsletter.html', context)

#In this function I cancel the subscription 
def newsletter_unsubscribe(request):
    form = NewsletterForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        #I first verify that the email entered by the user is in a table NewsLetterUser
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            #if email in table then delete this email and  Sending a farewell message
            NewsLetterUser.objects.filter(email=instance.email).delete()
            messages.success(request,f'تم الغاء الاشتراك  ')
            #"""Here I bring the email form and not from the table because the email was
           # already cleared from the table and then I send a farewell message"""
            subject = "شكرا للك"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            # with open(settings.BASE_DIR + "/templates/unsub_email.txt") as f:
            #     signup_message = f.read()
            signup_message = """ helo wel come """
            message = EmailMultiAlternatives(subject=subject,body=signup_message,from_email=from_email,to=to_email)
            html_template = get_template("unsub_email.html").render()
            message.attach_alternative(html_template,"text/html")
            message.send()
        else:
            messages.warning(request,f'هذا الايميل غير موجود ')
    context ={
        'form': form
    }   
    return render(request,'newsletter_unsubscribe.html', context)



#In this function I send new news to those who have registered in the mailing list
def control_newsletter(request):
    #I bring the amyla from a table NewsLetterUser I only take the values of the field
    getemail = NewsLetterUser.objects.all().values_list('email',flat=True).distinct()
    #And then convert the values  to list to ease send with function send_email
    email2=list(getemail)
    if request.method == 'POST':
        form = NewsCreationForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = settings.EMAIL_HOST_USER
            message = form.cleaned_data['message']
            email = email2
            try:
                send_mail(subject, message, from_email,email,fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('Success! Thank you for your message.')
    else:
        form = NewsCreationForm()       
    
    return render(request, 'control_newsletter.html', {'form': form})

