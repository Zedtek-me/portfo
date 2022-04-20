from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email= request.POST.get('Email')
        tel= request.POST.get('tel')
        msgs = request.POST.get('message')
        messages.success(request, f'Thank you for reaching out, {name}! Your message has been sent to me; \n I\'ll check through it soon.')
        print(request.POST)
        return redirect('index')
    msg= messages.get_messages(request)
    return render(request, 'index.html', {'msgs': msg})
    