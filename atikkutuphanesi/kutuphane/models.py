from django.db import models

# Create your models here.
class Atikcodes(models.Model):
    itsType = models.CharField(max_length=50, null=True)
    itsTtile = models.CharField(max_length=15, null=True)
    img = models.ImageField( null=True)
    warningContent = models.TextField(max_length=500, null=True)
    whereAccoursContent = models.TextField(max_length=500, null=True)
    howDefineContent = models.TextField(max_length=500, null=True)
    legislationlistContent = models.TextField(max_length=500, null=True)
    howToReduceContent = models.TextField(max_length=500, null=True)
    img2 =  models.ImageField( null=True)
    p1 = models.TextField(max_length=400, null=True)
    p2 = models.TextField(max_length=400, null=True)
    list1 = models.CharField(max_length=50, null=True)
    list2 = models.CharField(max_length=50, null=True)








    id = models.AutoField(primary_key=True)
    
    
    



