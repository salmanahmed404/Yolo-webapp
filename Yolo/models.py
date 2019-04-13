from django.db import models

class City(models.Model):
    city_name = models.CharField(max_length=50,primary_key=True)
    distance = models.IntegerField(default=0)

    def __str__(self):
        return self.city_name

