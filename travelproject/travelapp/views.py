from django.shortcuts import render
from .models import Place, Team


def travel(request):
    obj=Place.objects.all()
    obj2=Team.objects.all()
    return render(request,'index.html',{'result':obj,'result2':obj2})



