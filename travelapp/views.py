from django.shortcuts import render
from .models import Place
from .models import Team

# Create your views here.
def demo(request):
     obj=Place.objects.all()
     tem = Team.objects.all()
     return render(request,"index.html",{'result':obj,'temitem':tem})

# def tmitem(request):
#
#      return render(request,"index.html",{})