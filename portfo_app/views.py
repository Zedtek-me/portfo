from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == "POST":
        print(request.POST)
        name= request.POST.get('name')
        email= request.POST.get('Email')
        num= request.POST.get('tel')
        mgs= request.POST.get('message')
        messages.success(request, 'your information has been sent. thnaks!')
        return redirect('')
    else:
        msg=  messages.get_messages(request)
        return render(request, 'index.html', {'msg': msg})

