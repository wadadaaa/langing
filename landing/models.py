from django.db import models
from django.contrib.sites.models import Site
from colorful.fields import RGBColorField


class Page(models.Model):
    site = models.ForeignKey(Site)
    headline = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=250, blank=True)
    logo = models.ImageField(upload_to='logos')
    seo = models.CharField(max_length=250)


class Section(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    bg_img = models.ImageField(upload_to='bg_img')
    bg_color = RGBColorField(blank=True)


class Testimonials(models.Model):
    name = models.CharField(max_length=200)
    mention = models.CharField(max_length=250)
    avatar = models.ImageField(upload_to='avatars')

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'





