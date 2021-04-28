from django.db import models
from django.contrib.auth.models import User
from tags.models import Tags


class Newsletters(models.Model):

    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=250)
    target = models.IntegerField()
    frequency = models.CharField(max_length=100)
    votes = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='user_newsletter', on_delete=models.SET_NULL, null=True)
    members = models.ManyToManyField(User, related_name='members_user')
    tags = models.ManyToManyField(Tags)
