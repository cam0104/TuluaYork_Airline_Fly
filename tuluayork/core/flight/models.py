from django.db import models

class airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return  self.name

class requirement(models.Model):
    name = models.CharField(max_length=150, default='')

    def __str__(self):
        return  self.name

class airline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return  self.name


class flight(models.Model):
    airline = models.ForeignKey(airline, on_delete=models.CASCADE)
    airport_origin = models.ForeignKey(airport, on_delete=models.CASCADE, related_name="departures")
    airport_destination = models.ForeignKey(airport, on_delete=models.CASCADE, related_name="arrivals")
    depart_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    #scale =
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    requirements = models.ManyToManyField(requirement)
    n_seat = models.IntegerField()
    status = models.CharField(max_length=150)
















