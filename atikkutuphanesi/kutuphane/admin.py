from django.contrib import admin
from .models import Atikcodes
from.atiktypesmodels import Atiktypes,firstSteps,secondSteps,thirdSteps
from .models2 import buttonPart
from .contact import contact
class Codepanel_steps(admin.ModelAdmin):
     list_display = ("selfMark",)
     list_filter = ("upperMark",)
 
class Codepanel_type(admin.ModelAdmin):
     list_display = ("urlname",)
     
# Register your models here.
admin.site.register(Atikcodes)
admin.site.register(Atiktypes,Codepanel_type)
admin.site.register(firstSteps,Codepanel_steps)
admin.site.register(secondSteps,Codepanel_steps)
admin.site.register(thirdSteps,Codepanel_steps)
admin.site.register(contact)

#models2 içeriği panele ekle
admin.site.register(buttonPart)


