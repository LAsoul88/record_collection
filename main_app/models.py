from django.db import models
from django.db.models import Model, CharField, IntegerField, TextField, ForeignKey

# Create your models here.

class Record(Model):

    name = CharField(max_length=100)
    image = CharField(max_length=1000)
    year = IntegerField()
    artist = CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['year']


class Review(Model):

    review = TextField(max_length=1000)
    user = CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    record = ForeignKey(Record, on_delete=models.CASCADE, related_name="reviews")

    class Meta:
        ordering = ['created_at']


# Review
# text - written review of album
# record = FK Record(id)