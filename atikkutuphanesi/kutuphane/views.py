from django.shortcuts import render
from django.core import serializers

import pkg_resources

from kutuphane.models import Atikcodes
from . import models2
# atik listelerini burdan oluşturuyorum 

# Create your views here.
def index(request):
    return render(request,"index.html")

def works(request):
    return render(request,"works.html")

def about(request):
    return render(request,"about.html")

def atik_list(request,atikkind):
    #atikkind = "huseyin"
    if atikkind == "tibbiatik":
        return render(request,"atiklisttemplate.html")

def atikcode(request,id):
    atikcode = Atikcodes.objects.filter(id = id).first()
    
    if(atikcode!=None):
        return render(request,"atikcode.html",{"atikcode":atikcode})

def atik_uretimi(request,id):  
    return render(request,"atikuretimi.html",{"obje":models2.objeler[id],"kodlar":models2.objeler2[id]})

   



    

    