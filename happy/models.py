from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Service(models.Model):
    CATEGORY =(
        ('Individual Therapy','Individual Therapy'),
        ('Couples Therapy','Couples Therapy'),
        ('Teen Therapy','Teen Therapy'),
        ('Psychiatry','Psychiatry'),
        
    )
    
    category = models.CharField(max_length=50, null=True, choices=CATEGORY)
    description = models.CharField(max_length=800, null=True)
    
    # contact = models.ForeignKey(Contact,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.category
    # def get_contact_details(self):
    #     return{
    #         "":self.contact.,
    #         "":self.contact.,
    #         "":self.contact.,
    #         "":self.contact.,
    #         "":self.contact.,
    #     }
    
    def save_service(self):
        self.save() 

    def delete_service(self):
        self.delete()  
