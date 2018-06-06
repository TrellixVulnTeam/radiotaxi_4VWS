from django.db import models

COPYRIGHT='RIG'
COPYLEFT ='LEF'
CREATIVE_COMMONS = 'CC'

LICENSES = (
    (COPYRIGHT,'Copyright'),
    (COPYLEFT,'Copyleft'),
    (CREATIVE_COMMONS,'Creative Commons')
)

# Create your models here.
class User(models.Model):

    name= models.CharField(max_length = 150)
    url = models.URLField()
    description = models.TextField(blank=True,null=True,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    license = models.CharField(max_length=3,choices=LICENSES)

    def __str__(self):
        return self.title

#class Request(models.Model):

#    id=models.Aggregate
#    passanger==models.CharField


    def __str__(self):
        return title

#class Employee(models.Model):

#class Driver(models.Models):
#        def __str__(self):
#            return title

#class Billing(models.Model):

#class Branches(models.Model):

#class AddressLists(models.Model)



class Customers(models.Model):

    name=models.CharField(max_length=150)
    vat_code=models.CharField(max_length=20)
    code=models.IntegerField(null=False)
    address01= models.CharField(max_length=100)
    address02=models.CharField(max_length=100)
    address03 =models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by =models.CharField(max_length=20)
    country= models.CharField(max_length=25)



    #Campos nuevos fuera del modelo
    is_mandatory_pass_reg=models.BooleanField(default='False')

    def __str__(self):
        return self.title



#class CustomerSpecialFields(models.Model):
