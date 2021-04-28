from django.db import models


class Tags(models.Model):

    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
