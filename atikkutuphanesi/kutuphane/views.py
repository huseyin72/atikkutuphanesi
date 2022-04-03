from django.shortcuts import render
from django.core import serializers

import pkg_resources

from kutuphane.models import Atikcodes
from . import models2
from . import bannermodel
# atik listelerini burdan oluşturuyorum 

# Create your views here.
def index(request):
    return render(request,"index.html")

def works(request):
    return render(request,"works.html")

def about(request):
    return render(request,"about.html")

def atik_list(request,atikkind):
    #tıbbi atık 
    if atikkind == "tibbiatik":
        return render(request,"atiklisttemplate.html",{"tibbiatik":bannermodel.tibbi_atik})
    #atık lastik 
    elif atikkind == "atiklastik":
        return render(request,"atiklisttemplate.html",{"tibbiatik":bannermodel.atik_lastik})
    #atık yağ
    elif atikkind == "atikyag":
        return render(request,"atiklisttemplate.html",{"tibbiatik":bannermodel.atik_yag})
    #atık pil ve ak 
    elif atikkind == "atikpil":
        return render(request,"atiklisttemplate.html",{"tibbiatik":bannermodel.atik_pil})
    #bitkisel atık yağ 
    elif atikkind == "bitkiselatikyag":
        return render(request,"atiklisttemplate.html",{"tibbiatik":bannermodel.bitkisel_yag})
    #biyobozunur atık 
    elif atikkind == "biyobozunuratik":
        return render(request,"atiklisttemplate.html",{"tibbiatik":bannermodel.biyobozunur_atik})
        #ambalaj atık
    elif atikkind == "ambalajatik":
        return render(request,"atiklisttemplate.html",{"tibbiatik":bannermodel.ambalaj_atik})
        #ATIK ELEKTRİKLİ
    elif atikkind == "atikelektrik":
        return render(request,"atiklisttemplate.html",{"tibbiatik":bannermodel.atik_elektrik})
    


    

def atikcode(request,id):
    atikcode = Atikcodes.objects.first()
    
    """ if(atikcode!=None): """
    print(atikcode)
    return render(request,"atikcode.html",{"obje":atikcode})

def atik_uretimi(request,id):  
    return render(request,"atikuretimi.html",{"obje":models2.objeler[id],"kodlar":models2.objeler2[id]})

   
def contact(request):
    return render(request,"contact.html")


    

    