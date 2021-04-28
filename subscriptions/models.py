from django.contrib.auth.models import User
from newsletters.models import Newsletters
from django.db import models


class Subscriptions(models.Model):

    user = models.ForeignKey(User, related_name='user_subscription', on_delete=models.SET_NULL, null=True)
    newsletter = models.ForeignKey(Newsletters, related_name='newsletter_subscription', on_delete=models.SET_NULL, null=True)
