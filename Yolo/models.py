from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class City(models.Model):
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name


class Places(models.Model):
    place_name = models.CharField(max_length=50)
    lat = models.FloatField(max_length=10)
    lon = models.FloatField(max_length=10)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    city_name = models.ForeignKey(City, on_delete=models.CASCADE)
    def __str__(self):
        return self.place_name

class Events(models.Model):
    event_name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()

    place_name = models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    contact_no = models.CharField(max_length=100)

    place_name = models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Transport(models.Model):
    public_transport = models.CharField(max_length=100)

    place_name = models.ForeignKey(City,on_delete=models.CASCADE)

    means_of_transport = models.CharField(max_length=200)

    def __str__(self):
        return self.place_name

class Places_Of_Interest(models.Model):
    hotspot = models.CharField(max_length=100)
    place_name = models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return self.place_name

