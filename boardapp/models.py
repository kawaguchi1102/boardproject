from django.db import models


class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    images = models.ImageField(upload_to='')
    good = models.IntegerField()
    read = models.IntegerField()
    read_text = models.CharField(max_length=200)
