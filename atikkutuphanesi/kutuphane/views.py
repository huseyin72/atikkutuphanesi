
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages




from kutuphane.models import Atikcodes
from kutuphane.atiktypesmodels import Atiktypes,firstSteps,secondSteps,thirdSteps
from . import models2
from . import bannermodel
from kutuphane.models2 import buttonPart
from kutuphane.contact import contact
# atik listelerini burdan oluşturuyorum 

# Create your views here.
def home(request):
    return render(request,"home.html")
def index(request):
    return render(request,"index.html")

def works(request):
    return render(request,"works.html")

def about(request):
    return render(request,"about.html")

def atik_list(request,atikkind):
    #tıbbi atık 
    the_content = Atiktypes.objects.filter(urlname = atikkind)
    firstS = firstSteps.objects.filter(upperMark = atikkind)
    secondS = secondSteps.objects.all()
    thirdS = thirdSteps.objects.all()
    
    
    firstSset = []
    secondSset = []
    thirdSet = []

    theQueryA = []
    theQueryB = []

    # ilk dropdown sorgusu
    for k in firstS:
        firstSset1 = firstSteps()
        firstSset1.content = k.content
        firstSset1.upperMark = k.upperMark
        firstSset1.selfMark = k.selfMark
        firstSset.append(firstSset1)
        varB = k.selfMark
        theQueryA.append(varB)

    #ikinci dropdown sorgusu
    for l in secondS:
        if l.upperMark in theQueryA:
            secondSset1 = secondSteps()
            secondSset1.content = l.content
            secondSset1.upperMark = l.upperMark
            secondSset1.selfMark = l.selfMark
            secondSset.append(secondSset1)
            
            theQueryB.append(l.selfMark)
            
    for j in thirdS:
        if j.upperMark in theQueryB:
            thirdSet1 = thirdSteps()
            thirdSet1.content = j.content
            thirdSet1.upperMark = j.upperMark
            thirdSet1.selfMark = j.selfMark
            thirdSet1.href = j.href
            thirdSet.append(thirdSet1)

    
    data = Atiktypes()
    for i in the_content:
        data.urlname = i.urlname
        data.whatIsIt = i.whatIsIt
        data.whyİmportant = i.whyİmportant
        data.whereAccours = i.whereAccours
        data.howUnderstand = i.howUnderstand
        data.mainname = i.mainname
        #içeriği bitir

   
    

    for i in firstSset:
        print(i.content)
    
    return render(request,"atiklisttemplate.html",{"data":data,"firstStep":firstSset,"secondStep":secondSset,"thirdStep":thirdSet})
    """ if atikkind == "tibbiatik":
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
     """


    

def atikcode(request,id):
    atikcode = Atikcodes.objects.first()
    
    """ if(atikcode!=None): """
    print(atikcode)
    return render(request,"atikcode.html",{"obje":atikcode})




def atik_uretimi(request,atikuretimi):
    filter = buttonPart.objects.filter(urlName = atikuretimi)
    theObject = buttonPart()
    for k in filter:   
        theObject.urlName = k.urlName
        theObject.prosesFeatures = k.prosesFeatures
        theObject.mainName = k.mainName
        theObject.atikoneri = k.atikoneri
        theObject.nace = k.nace
        theObject.files = k.files
        theObject.prosesKaynakli = k.prosesKaynakli.split(".")
        theObject.olusabilecek_diger = k.olusabilecek_diger.split(".")
    
    


    return render(request,"atikuretimi.html",{"data":theObject})


def contact1(request):
    print(request.method)
    
    if request.method == "POST":
        print("girdim")
        form = contact()
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        form.name = name
        form.email = email
        form.message = message
        form.save()
        
        
        messages.success(request,"Mesajınız başarıyla iletildi")
        return redirect("/contact")
    print("selam")

  
    
         

    return render(request,"contact.html")


    

