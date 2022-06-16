from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def index(request):
    if request.method == 'POST':
        # get all details from the form
        name = request.POST.get('name')
        email= request.POST.get('Email')
        tel= request.POST.get('tel', None)
        msgs = request.POST.get('message')
        print(type(request))
        # send an email message to myself
        send_mail(
            subject='FROM A RECRUITER!', 
            message=f'''
                        {name}; {email}; {tel}; sent:\n 
                        {msgs}
                    ''',
            from_email='Zedtek@djangoportfolio',
            recipient_list=['zechmanad@yahoo.com'],
            fail_silently=False
            )
        # send a feedback to the sender
        messages.success(request, f'Thank you for reaching out, {name}! Your message has been sent to me; \n I\'ll check through it soon.')
        return redirect('index')
    msg= messages.get_messages(request)
    return render(request, 'index.html', {'msgs': msg})
    