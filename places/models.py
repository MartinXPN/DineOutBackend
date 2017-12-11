from django.core.validators import RegexValidator
from django.db import models
from django.db.models import CharField, FloatField, URLField, ForeignKey, OneToOneField, DecimalField


class PlaceInfo(models.Model):
    description = CharField(max_length=150)
    # workingHours
    # priceRange
    # music
    # cuisine

    def __str__(self):
        return self.description


class Address(models.Model):
    latitude = DecimalField(max_digits=19, decimal_places=10)
    longitude = DecimalField(max_digits=19, decimal_places=10)
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Service(models.Model):
    description = CharField(max_length=50)
    logoURL = URLField(max_length=200, name='service-logo')
    # wifi
    # privateRooms
    # banquet
    # shipping
    # acceptsCreditCard
    # parking
    # insideSeating
    # outsideSeating
    # smokingAreas
    # smokeFreeAreas

    def __str__(self):
        return self.description


class Place(models.Model):
    name = CharField(max_length=50, default='')
    shortDescription = CharField(max_length=1000)
    rating = FloatField(default=5)
    logoURL = URLField(max_length=200, name='logo')

    def __str__(self):
        return self.name + '\trating: ' + str(self.rating)


class PlaceBranch(models.Model):
    place = ForeignKey(Place, on_delete=models.CASCADE, related_name='branches')
    address = OneToOneField(Address, on_delete=models.CASCADE, primary_key=True)
    services = models.ManyToManyField(Service)
    placeInfo = models.ManyToManyField(PlaceInfo)

    def __str__(self):
        return self.place.name + '\tlocated at: ' + self.address.name


class Image(models.Model):
    url = URLField(max_length=300)
    branch = ForeignKey(PlaceBranch, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.url


class PhoneNumber(models.Model):
    place = ForeignKey(PlaceBranch, on_delete=models.CASCADE, related_name='phoneNumbers')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number format must be: '+999999999'. Up to 15 digits.")
    phoneNumber = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return str(self.phoneNumber)
