from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Food

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = '__all__'