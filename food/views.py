from food.models import Dishes
from django.shortcuts import render
from .models import Dishes
# Create your views here.

def index(request):

    dish = Dishes.objects.all()
    
    return render(request, "index.html",{'dish': dish})
