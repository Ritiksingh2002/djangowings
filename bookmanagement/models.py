from django.db import models

# Create your models here.

class CreateBook(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    sold = models.BooleanField(default=True)
    language= models.CharField(max_length=20)


#Model (CreateBook)  -->  Serializer (CreateBookSerializer)  -->  ViewSet (CreateBookViewSet)  -->  Router + URLs  --> Client (Postman, frontend)
