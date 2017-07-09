# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib import admin
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth.models import User
from unidecode import unidecode


def upload_location(post, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    return "%s/%s" %(post.id, filename)

class Travels(models.Model):
    title_region  = models.CharField(max_length=230,null=True,)
    region  = models.CharField(max_length=230,null=True)
    district  = models.CharField(max_length=230,null=True)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return u"%s %s %s "%(self.title_region,self.region,self.district)


    def __str__(self):
        return u"%s %s %s"%(self.title_region,self.region,self.district)

    def get_absolute_url(self):
        return reverse("list:detail", kwargs={"slug": self.slug})


class Post(models.Model):
    travels = models.ForeignKey(Travels,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            width_field="width_field",
            height_field="height_field",verbose_name=u'Фото локації', help_text='150x150px'
                              )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    content = RichTextField()
    timestamp = models.DateTimeField(null=True)
    author = models.ForeignKey(User)



    def __unicode__(self):
        return u"%s %s "%(self.title,self.content)


    def __str__(self):
        return u"%s %s"%(self.title,self.content)

    def get_absolute_url(self):
        return reverse("list:detail", kwargs={"slug": self.slug})


def create_slug(post,new_slug=None):
    slug = slugify(unidecode(post.title))
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = unidecode("%s-%s"%(slug,qs.first().id))
        return create_slug(post,new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, post, *args, **kwargs):
    if not post.slug:
        post.slug = unidecode(create_slug(post))



pre_save.connect(pre_save_post_receiver, sender=Post)

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unidecode(create_slug(instance))



pre_save.connect(pre_save_post_receiver, sender=Post)