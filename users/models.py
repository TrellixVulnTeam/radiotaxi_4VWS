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

class Trip(models.Model):

#    id=models.Aggregate
#    passanger==models.CharField



    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by =models.CharField(max_length=20)


    def __str__(self):
        return title

class Employee(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by =models.CharField(max_length=20)


    def __str__(self):
        return title


class Driver(models.Model):

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    national_id=models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by =models.CharField(max_length=20)


    def __str__(self):
        return title

#class Billing(models.Model):

class Customers(models.Model):

    name = models.CharField(max_length=150)
    vat_code = models.CharField(max_length=20)
    code = models.IntegerField(null=False)
    address01 = models.CharField(max_length=100)
    address02 = models.CharField(max_length=100)
    address03 = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by =models.CharField(max_length=20)
    country = models.CharField(max_length=25)



    #Campos nuevos fuera del modelo
    is_mandatory_pass_reg=models.BooleanField(default='False')

    def __str__(self):
        return self.title


class Aggrement(models.Model):

    customer=models.ForeignKey(Customers,on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Branches(models.Model):

    def __str__(self):
        return self.title



class Contacts(models.Model):


    customer=models.ForeignKey(Customers,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by =models.CharField(max_length=20)

    def __str__(self):
        return self.title


class AddressLists(models.Model):

    is_favorite = models.CharField(max_length=1)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by =models.CharField(max_length=20)



    def __str__(self):
        return self.title

class Passenger(models.Model):
    username=models.CharField(max_length=25)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=50)
    gender=models.IntegerField()
    date_birth=models.DateField()
    email=models.EmailField()

    customer=models.ForeignKey(Customers,on_delete=models.CASCADE)


    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by =models.CharField(max_length=20)


    def __str__(self):
        return self.title


class Special_Fields(models.Model):


    customer=models.ForeignKey(Customers,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by =models.CharField(max_length=20)

    def __str__(self):
        return self.title




#class CustomerSpecialFields(models.Model):
