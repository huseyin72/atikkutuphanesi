from django.db import models

# Create your models here.
class Atikcodes(models.Model):
    id = models.AutoField(primary_key=True)
    
    atikname = models.CharField(max_length=50)
    atik_features = models.TextField(max_length=60)
    where_to_go = models.TextField(max_length=50)
    atik_advice = models.TextField(max_length=100)
    klavuz = models.CharField(max_length=30)
    



