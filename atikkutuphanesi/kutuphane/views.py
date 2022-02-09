from django.shortcuts import render
from django.core import serializers

import pkg_resources

from kutuphane.models import Atikcodes

# Create your views here.
def index(request):
    return render(request,"index.html")

def works(request):
    return render(request,"works.html")

def about(request):
    return render(request,"about.html")
def atik_list(request):
    return render(request,"atiklist.html")
def atikcode(request,id):
    atikcode = Atikcodes.objects.filter(id = id).first()
    
    if(atikcode!=None):
        return render(request,"atikcode.html",{"atikcode":atikcode})



   



    

    