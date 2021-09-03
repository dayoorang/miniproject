from django.db import models

# Create your models here.


SEX_CHOICES = (
            ('Female', 'Female' ),
            ('Male', 'Male' ),

)
class Animal(models.Model):
    sex = models.CharField(max_length=100, blank=False, null=False, choices=SEX_CHOICES)
    image = models.ImageField(upload_to='face/', blank=False, null=False)