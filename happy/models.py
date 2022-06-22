from django.db import models
# Create your models here.

class Contact(models.Model):
    first_name= models.CharField(max_length=150)
    last_name= models.CharField(max_length=150)
    email= models.CharField(max_length=150)
    phone_number= models.CharField(max_length=150)
    location= models.CharField(max_length=150)

    def __str__(self):
        return self.first_name
   
    # def save_contact(self):
    #     self.save() 

    # def delete_contact(self):
    #     self.delete()  
