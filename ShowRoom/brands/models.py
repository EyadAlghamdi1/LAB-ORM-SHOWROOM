from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True) 
    logo = models.ImageField(upload_to='images/')  
    about = models.TextField()  
    founded_at = models.DateField() 
    website = models.URLField(blank=True, null=True)  
    def __str__(self) -> str:
      return self.name