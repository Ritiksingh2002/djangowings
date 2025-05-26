from django.db import models

# Create your models here.
# Field	Type	Notes
# id	integer	Primary key, autoincrement (default in Django)
# name	string	
# category	string	
# price	integer	
# quantity	integer	
# barcode	integer	Unique=True

class Item(models.Model):
   name = models.CharField(max_length=40)
   category= models.CharField(max_length=40)
   price= models.IntegerField()
   quantity= models.IntegerField()
   barcode= models.IntegerField(unique=True)

   def __str__(self):
    return self.name
