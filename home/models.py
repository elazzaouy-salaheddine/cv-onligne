from django.db import models
from django.db.models.base import Model
from django.db.models.fields import EmailField

# Create your models here.


class About(models.Model):
    logo = models.ImageField(upload_to='profile')
    intor = models.TextField()
    full_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    birthday = models.DateField()
    website = models.URLField()
    degree = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    phEmailone = models.EmailField()
    city = models.CharField(max_length=255)
    description = models.TextField()

class Facts(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=255)

class Skills(models.Model):
    title= models.CharField(max_length=255)
    valeu = models.IntegerField()

class Resume_Education(models.Model):
    degree = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    institute_name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)

class Resume_Professional_Experience(models.Model):
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    details = models.TextField()


class Portfolio_Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category
        

class Portfolio_Itemes(models.Model):
    category = models.ForeignKey(Portfolio_Category,on_delete=models.CASCADE)
    client = models.CharField(max_length=255)
    project_date = models.DateField()
    project_url = models.URLField()
    description = models.TextField()
    image = models.ImageField(upload_to='porfolio')


class Service(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    icone = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Testimonials(models.Model):
    body = models.TextField()
    client_name = models.CharField(max_length=255)
    job_client = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='clients/', height_field=None, width_field=None, max_length=None)

class Contact(models.Model):
    description = models.TextField()
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)

class Social_links(models.Model):
    social_name = models.CharField(max_length=50)
    social_link = models.URLField(max_length=200)