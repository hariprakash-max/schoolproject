from django.db import models
from django.db import models
class student(models.Model):   
    name=models.CharField(max_length=100)
    fathername=models.CharField(max_length=100)
    classname=models.IntegerField()
    contact=models.CharField(max_length=100)
    
#------------------------------------------------------------
# from django.db import models  
class Teacher(models.Model): 
    name = models.CharField(max_length=100) 
    exp = models.IntegerField() 
    subject = models.CharField(max_length=100) 
    contact = models.CharField(max_length=100)  
    
#--------------------------------------------------------------  
    
from django.urls  import reverse 
from django.db import models  
class Teacher(models.Model): 
    name = models.CharField(max_length=100) 
    exp = models.IntegerField() 
    subject = models.CharField(max_length=100) 
    contact = models.CharField(max_length=100) 

def get_absolute_url(self): 
    return reverse('listteacher') 
def get_absolute_url(self): 
    return reverse('listteacher',kwargs={'pk':self.pk})

# --------------------------------------------------------------
