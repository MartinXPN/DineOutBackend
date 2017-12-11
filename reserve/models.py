from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from django.db.models import ForeignKey, PositiveSmallIntegerField, CharField, DateTimeField

from places.models import PlaceBranch


class Reservation(models.Model):
    placeBranch = ForeignKey(PlaceBranch, on_delete=models.CASCADE)
    user = ForeignKey(User, on_delete=models.CASCADE)

    date = DateTimeField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number format must be: '+999999999'. Up to 15 digits.")
    phoneNumber = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    # ensure that group size is a positive integer with value smaller than 20
    groupSize = PositiveSmallIntegerField(validators=[
            MaxValueValidator(20),
            MinValueValidator(1)
        ])

    status = CharField(max_length=1, default='q', choices=(
        ('c', 'canceled'),      # User cancels reservation
        ('r', 'reserved'),      # Reservation was successful
        ('q', 'requested'),     # User requests reservation
        ('f', 'failed'),        # Reservation wasn't successful (no enough room, etc...)
    ))
