from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Sum

from main_app.models import Food
# Define the home view
def home(request):
  return render(request,'home.html')

def about(request):
  data = Food.objects.aggregate(
    Sum('calories'), 
    Sum('protein'), 
    Sum('carbohydrates'), 
    Sum('fat'), 
    Sum('fiber'))
  return render(request, 'about.html', {'data':data})
# PNH8MnUSvxfXfIl2BJ9czQ==KxF5yVwD8rPHe16v
def api(request):
  import json
  import requests
  if request.method == 'POST':
        query = request.POST['query']
        api_request = requests.get('https://api.api-ninjas.com/v1/nutrition?query=' + query, headers={'X-Api-Key': 'PNH8MnUSvxfXfIl2BJ9czQ==KxF5yVwD8rPHe16v'})
        api = json.loads(api_request.content)
        return render(request, 'api.html', {'api': api})
  else:
        return render(request, 'api.html', {'query': 'Enter a valid query'})

def foods_index(request):
  foods=Food.objects.all()
  data = Food.objects.aggregate(
    Sum('calories'), 
    Sum('protein'), 
    Sum('carbohydrates'), 
    Sum('fat'), 
    Sum('fiber'))
  return render(request, 'foods/index.html', {'foods':foods, 'data':data})

def foods_detail(request, food_id):
  food=Food.objects.get(id=food_id)
  return render(request, 'foods/detail.html', {'food':food})

class FoodsCreate(CreateView):
  model = Food
  fields=('name', 'calories','carbohydrates', 'protein', 'fat' , 'fiber')
  success_url = '/foods/'
class FoodsUpdate(UpdateView):
  model = Food
  fields = ('name', 'calories','carbohydrates', 'protein', 'fat' , 'fiber')
  success_url = '/foods/'

class FoodsDelete(DeleteView):
  model = Food
  success_url = '/foods/'


