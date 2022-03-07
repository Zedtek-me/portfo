from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def thanks(req):
    if req.method == 'POST':
        req.post.get()
    else:
        pass
    return render(req, 'thanks.html',{})