from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404,Http404
from django.contrib import messages
from .models import NewsLetterUser
from django.http import HttpResponse
from .forms import ,NewsletterForm,NewsCreationForm
from django.conf import settings
from django.core.mail import send_mail, get_connection,BadHeaderError,EmailMultiAlternatives





def newsletter_singup(request):
    now = timezone.now()
    form = NewsletterForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            messages.warning(request,f'هذا الايميل مشترك مسبقا')
        else:
            instance.save()
            messages.success(request,f'تم الاشتراك بنجاح ')
            subject = " الاشتراك البريدي"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            # with open(settings.BASE_DIR + "/templates/sign_up_email.txt") as f:
            #     signup_message = f.read()
            signup_message = """ helo wel come """
            message = EmailMultiAlternatives(subject=subject,body=signup_message,from_email=from_email,to=to_email)
            html_template = get_template("sign_up_email.html").render()
            message.attach_alternative(html_template,"text/html")
            message.send()
    context ={
         'year':now,
        'form': form
    }   
    return render(request,'newsletter.html', context)

def newsletter_unsubscribe(request):
    now = timezone.now()
    form = NewsletterForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            NewsLetterUser.objects.filter(email=instance.email).delete()
            messages.success(request,f'تم الغاء الاشتراك  ')
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
         'year':now,
        'form': form
    }   
    return render(request,'newsletter_unsubscribe.html', context)




def control_newsletter(request):
    getemail = NewsLetterUser.objects.all().values_list('email',flat=True).distinct()
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

