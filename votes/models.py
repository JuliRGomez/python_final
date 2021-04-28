from django.db import models
from django.contrib.auth.models import User
from newsletters.models import Newsletters


class Votes(models.Model):

    user = models.ForeignKey(User, related_name='user_vote', on_delete=models.SET_NULL, null=True)
    newsletter = models.ForeignKey(Newsletters, related_name='newsletter_vote', on_delete=models.SET_NULL, null=True)
