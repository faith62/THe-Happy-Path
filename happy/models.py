from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    first_name= models.CharField(max_length=150)
    last_name= models.CharField(max_length=150)
    email= models.CharField(max_length=150)
    phone_number= models.CharField(max_length=150)
    location= models.CharField(max_length=150)

    def __str__(self):
        return self.first_name

class Service(models.Model):
    CATEGORY =(
        ('Individual Therapy','Individual Therapy'),
        ('Couples Therapy','Couples Therapy'),
        ('Teen Therapy','Teen Therapy'),
        ('Psychiatry','Psychiatry'),
        
    )
    
    category = models.CharField(max_length=50, null=True, choices=CATEGORY)
    description = models.CharField(max_length=800, null=True)    
    contact = models.ForeignKey(Contact,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.category
    def get_contact_details(self):
        return{
            "first_name":self.contact.first_name,
            "last_name":self.contact.last_name,
            "email":self.contact.email,
            "phone_number":self.contact.phone_number,
            "location":self.contact.location,
        }
    
    def save_service(self):
        self.save() 

    def delete_service(self):
        self.delete()  



   
   