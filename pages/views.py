from django.shortcuts import render

# Create your views here.
def aboutus(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def error(request):
    return render(request, 'error-404.html')