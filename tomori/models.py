from django.db import models
from django.contrib.auth.models import User


class article(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)
    username = models.ForeignKey(User)

    def __unicode__(self):
        return self.title
