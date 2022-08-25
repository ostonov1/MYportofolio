from django.db import models


class Message(models.Model):
    ism = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    xabar = models.TextField()
    sub = models.TextField()


class Portofolio(models.Model):
    img = models.ImageField()
    text = models.TextField()
