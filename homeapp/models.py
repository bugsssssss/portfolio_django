from pyexpat import model
from statistics import mode
from tabnanny import verbose
from turtle import title
from django.db import models
from django.forms import forms, widgets
from django import forms
from django.urls import reverse

class Feedback(models.Model): 

    name = models.CharField('name', max_length=100)
    email = models.EmailField('email', max_length=60)
    text = models.TextField('text', max_length=255)


    def __str__(self):
        return f'{self.name}'



    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

 
class Service(models.Model):

    icon = models.ImageField(("icon"), upload_to='icons_pack', null=True, blank=True)
    title = models.CharField(("title"), max_length=100)
    description = models.CharField(("description"), max_length=255)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return f'{self.title}'



class Portfolio(models.Model):
    image = models.ImageField(("image"), upload_to='portfolio_images')
    title = models.CharField(("title"), max_length=100)
    text = models.CharField(("text"), max_length=100)



 
class Testimonial(models.Model):

    picture = models.ImageField(("picture"), upload_to='profile')
    name = models.CharField(("name"), max_length=100)
    text = models.CharField(("text"), max_length=255)

    class Meta:
        verbose_name = ("Testmonial")
        verbose_name_plural = ("Testmonials")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Testmonial_detail", kwargs={"pk": self.pk})
