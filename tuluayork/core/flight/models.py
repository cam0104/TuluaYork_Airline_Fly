from django.db import models
from datetime import datetime
from django.conf import settings
from crum import get_current_user
from django.db.models.deletion import CASCADE

class airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class requirement(models.Model):
    name = models.CharField(max_length=150, default="")

    def __str__(self):
        return self.name


class airline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class flight(models.Model):
    airline = models.ForeignKey(airline, on_delete=models.CASCADE)
    airport_origin = models.ForeignKey(
        airport, on_delete=models.CASCADE, related_name="departures"
    )
    airport_destination = models.ForeignKey(
        airport, on_delete=models.CASCADE, related_name="arrivals"
    )
    destination_name = models.CharField(max_length=200, default='')
    depart_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    # scale =
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    requirements = models.ManyToManyField(requirement)
    n_seat = models.IntegerField()
    status = models.CharField(max_length=150)

    def __str__(self):
        return str(self.airline)


class booking(models.Model):
    user_reservation = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name="actual_user",
        null=True,
        blank=True,
    )
    flight = models.ForeignKey(flight, on_delete=models.CASCADE)
    date_reservation = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_reservation = user
            else:
                self.user_reservation = user
        super(booking, self).save()

    def __str__(self):
        return str(self.user_reservation)
