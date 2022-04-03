from django.db import models

class Atiktypes(models.Model):
     urlname = models.CharField(max_length=50)
     whatIsIt = models.TextField(max_length=500)
     whyİmportant =  models.TextField(max_length=500)
     whereAccours =  models.TextField(max_length=500)
     howUnderstand =  models.TextField(max_length=700)
     mainname = models.CharField(max_length=50)
     


class AtiktypesCodes(models.Model):
     urlName = models.CharField(max_length=50)
     codeName = models.CharField(max_length=50)