from django.db import models
from autoslug import AutoSlugField
from django import forms
from customer.models import Customer
from django.utils.translation import gettext_lazy as _

class MovieGenre(models.Model):

    label=models.CharField(max_length=50, blank=True, null=True)
    slug=AutoSlugField(populate_from="label", null=True)
    
class Movie(models.Model):

    actors= models.CharField(max_length=50, blank=True, null=True)
    country=models.CharField(max_length=50, blank=True, null=True)
    director=models.CharField(max_length=50, blank=True, null=True, verbose_name=_("réalisateur"))
    length= models.TimeField(auto_now=False, auto_now_add=False)
    picture=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True, null=True)
    release_date=models.DateField()
    rented=models.BooleanField()
    slug=AutoSlugField(populate_from="title", null=True)
    synopsis=models.TextField(blank=True, null=True)
    title=models.CharField(max_length=50)
    trailer_url=models.URLField(max_length=200, blank=True, null=True )
    genres=models.ManyToManyField(MovieGenre)

    

    def __unicode__(self):
        return self.title

    def is_rented (self):
        rented = self.rents.filter(date_retur=None).count() !=0
        return rented

    

class MovieRent(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE, related_name="rents")
    date_out = models.DateField(auto_now_add=True)
    date_retur = models.DateField(blank=True,null = True)


