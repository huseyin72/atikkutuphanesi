from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('works/', views.works,name="works"),
    path('about/', views.about,name="about"),
    path('atiklist/', views.atik_list,name="atiklist"),
    path('atikkod/<int:id>', views.atikcode,name="atikcode"),
   
    

]
