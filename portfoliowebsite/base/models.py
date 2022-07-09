from statistics import mode
from turtle import title
from django.db import models
import uuid
from django.db.models import Func

class Month(Func):
    function = 'STRFTIME'
    template = '%(function)s("%%m", %(expressions)s)'
    output_field = models.TextField()

class Year(Func):
    function = 'STRFTIME'
    template = '%(function)s("%%Y", %(expressions)s)'
    output_field = models.TextField()

class Project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    body = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    id = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)

    def __str__(self) -> str:
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    id = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)

    def __str__(self) -> str:
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    id = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)

    def __str__(self) -> str:
        return self.name

class PBI_articles(models.Model):
    Article_title = models.CharField(max_length=200)
    Article_date = models.DateField()
    Article_short_text = models.TextField(null=True, blank=True)
    Aricle_list_tags = models.TextField(null=True, blank=True)
    Article_post_link = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    def tags_as_list(self):
        return self.Aricle_list_tags.split(',')

class Last_Refreshh(models.Model):
    DateTime = models.DateTimeField()
    Nickname = models.CharField(max_length=100)

class Google_trends(models.Model):
    DateTime = models.DateField()
    PowerBi_trend = models.IntegerField()
    Tableau_trend = models.IntegerField()
    Qlik_trend = models.IntegerField()