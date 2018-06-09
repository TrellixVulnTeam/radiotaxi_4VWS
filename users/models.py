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


class Passenger(models.Model):



    national_id= models.CharField
    first_name=models.CharField
    last_name=models.CharField
    date_birth=models.DateField

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by =models.CharField(max_length=20)


    def __str__(self):
        return self.first_name


class Vehicle(models.Model):



    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by =models.CharField(max_length=20)
    year= models.IntegerField
    model=models.CharField
    brand=models.CharField
    type_v=models.CharField



    def __str__(self):
        return self.created_at


class TripTracking(models.Model):


    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by =models.CharField(max_length=20)

    def __str__(self):
            return self.created_at

class Driver(models.Model):

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    national_id=models.CharField(max_length=20)

    licence_type=models.CharField(max_length=20)
    date_birth = models.DateField()

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
        return self.name



class Aggrement(models.Model):

    customer=models.ForeignKey(Customers,on_delete=models.CASCADE)
    def __str__(self):
        return self.customer.name
#este es el objeto que configura el Movil que se encuentra configurado con Vehiculo y Conductor
class Transport(models.Model):


    vehicle =models.ForeignKey(Vehicle,on_delete=models.PROTECT)
    driver= models.ForeignKey(Driver,on_delete = models.PROTECT)


    start_service_dt = models.DateTimeField
    end_service_dt = models.DateTimeField

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by =models.CharField(max_length=20)


    def __str__(self):
        return self.start_service_dt


class Trip(models.Model):

#    id=models.Aggregate
#    passanger==models.CharField
    id_transport=models.IntegerField
    #passenger = models.ForeignKey(Passenger,on_delete=models.PROTECT)
    transport= models.ForeignKey(Transport,on_delete = models.PROTECT)
    customer= models.ForeignKey(Customers,on_delete = models.PROTECT)
    aggrement = models.ForeignKey(Aggrement, on_delete = models.PROTECT)

    area = models.CharField(max_length=30)

    pickup_address = models.CharField(max_length=150)
    destination_address = models.CharField(max_length=150)

    phone=models.CharField(max_length=20)
    mobile_phone=models.CharField(max_length=20)
    payment_term = models.CharField(max_length=20)
    comments= models.CharField(max_length=100)

    start_trip_dt = models.DateTimeField
    end_trip_dt = models.DateTimeField

    ticket_number = models.IntegerField

    amount = models.IntegerField

    reported_pass = models.BooleanField()

    current_status=models.CharField(max_length=20)
    cost_center=models.CharField(max_length=10)

    modified_pass=models.BooleanField
    modified_pass_dt=models.DateTimeField

    engange_dt = models.DateTimeField

    cancellation_type= models.CharField
    cancellation_comments = models.CharField

    tag_quantity=models.IntegerField
    tag_amount=models.IntegerField

    operator = models.CharField


    #Bank aggrement

    metres_trip = models.IntegerField
    wait_time = models.TimeField

    others = models.CharField

    park_amount = models.IntegerField

    toll_amount = models.IntegerField
















    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by =models.CharField(max_length=20)


    def __str__(self):
        return self.area


class ExtraServices(models.Model):



    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by =models.CharField(max_length=20)


    def __str__(self):
        return self.title


class Employee(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by =models.CharField(max_length=20)


    def __str__(self):
        return title






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
