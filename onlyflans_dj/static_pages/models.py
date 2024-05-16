from django.db import models
import uuid

# Create your models here.
class Flan(models.Model): 
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0.00)
    
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
        

class Cliente(models.Model):
    cliente_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)

