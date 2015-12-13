from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    username = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

class Top(models.Model):
    text = models.TextField()
    username = models.ForeignKey(User)

    def __unicode__(self):
        return self.text

class Menu(models.Model):
    text = models.TextField()
    username = models.ForeignKey(User)

    def __unicode__(self):
        return self.text

class Option(models.Model):
    argument = models.CharField(max_length=100)
    param = models.CharField(max_length=100)

    def __unicode__(self):
        return self.param

