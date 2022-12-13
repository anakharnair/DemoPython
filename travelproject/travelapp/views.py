from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Person

# Create your views her


def demo(request):
   obj=Place.objects.all()
   objs=Person.objects.all()

   return render(request,"index.html",{'result':obj,'results':objs})


