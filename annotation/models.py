from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=100)

class Document(models.Model):
    content = models.TextField(max_length=1000)

class Annotation(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
