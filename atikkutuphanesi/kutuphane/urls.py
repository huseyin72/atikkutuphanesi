from django.contrib import admin
from django.urls import path,include
from . import views
#from django.conf.urls import url
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('wastenavigation/', views.index,name="index"),
    path('works/', views.works,name="works"),
    path('about/', views.about,name="about"),
    path('atiklist/<str:atikkind>', views.atik_list,name="atiklist"),
    path('atikkod/<int:id>', views.atikcode,name="atikcode"),
    path('atikuretimi/<str:atikuretimi>', views.atik_uretimi,name="atik_uretimi"),
    path('contact', views.contact1, name="contact")
   
    

]
