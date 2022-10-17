from django.shortcuts import render
import requests

# Define the home view
def home(request):
  return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
  response=requests.get('https://api.covid19api.com/countries').json()
  return render(request, 'index.html', {'response':response})