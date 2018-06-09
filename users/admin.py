from django.contrib import admin
from .models import User
from .models import Customers
from .models import Trip
from .models import Aggrement
from .models import Transport
from .models import AddressLists
from .models import Vehicle
from .models import Driver
from .models import Employee


# Register your models here.

admin.site.register(User)
admin.site.register(Customers)
admin.site.register(Trip)
admin.site.register(Vehicle)
admin.site.register(Transport)
admin.site.register(Driver)
admin.site.register(AddressLists)
