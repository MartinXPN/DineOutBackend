from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import ForeignKey, PositiveSmallIntegerField

from places.models import PlaceBranch


class Reservation(models.Model):
    place = ForeignKey(PlaceBranch, on_delete=models.CASCADE)
    user = ForeignKey(User, on_delete=models.CASCADE)
    # ensure that group size is a positive integer with value smaller than 20
    groupSize = PositiveSmallIntegerField(validators=[
            MaxValueValidator(20),
            MinValueValidator(1)
        ])
