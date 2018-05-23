from django.db import models

COPYRIGHT='RIG'
COPYLEFT ='LEF'
CREATIVE_COMMONS = 'CC'

LICENSES = (
    (COPYRIGHT,'Copyright'),
    (COPYLEFT,'CopyLeft'),
    (CREATIVE_COMMONS,'Creative Commons')

)

# Create your models here.
class User(models.Model):

    name= models.CharField(max_length = 150)
    url = models.URLField()
    description = models.TextField(blank=,null=true,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    licence = models.CharField(max_length="3",choices=LICENSES)
