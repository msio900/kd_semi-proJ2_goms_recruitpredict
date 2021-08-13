from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')
def home(request):
    return render(request, 'index.html')
def index(request):
    return render(request, 'index.html')
def elements(request):
    return render(request, 'elements.html')
def generic(request):
    return render(request, 'generic.html')