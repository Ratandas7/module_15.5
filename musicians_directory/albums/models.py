from django.db import models
from musicians . models import Musician
# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_release_date = models.DateField(auto_now=True)
    RATING_CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    album_rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return f"Album Name : {self.album_name}"

