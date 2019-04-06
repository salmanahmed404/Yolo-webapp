from django.db import models

class City(models.Model):
    city_name = models.CharField(max_length=50,primary_key=True)

    def __str__(self):
        return self.city_name

class Places(models.Model):
    place_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    
    city_name = models.ForeignKey(City, on_delete=models.CASCADE)
    def __str__(self):
        return self.place_name

class Events(models.Model):
    event_name = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()
    exists = models.BooleanField()


    place_name = models.ForeignKey(Places,on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    dist = models.FloatField()

    place_name = models.ForeignKey(Places,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Places_Of_Interest(models.Model):
    hotspot = models.CharField(max_length=100)

    place_name = models.ForeignKey(Places,on_delete=models.CASCADE)

    def __str__(self):
        return self.place_name
