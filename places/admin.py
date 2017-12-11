from django.contrib import admin

from places.models import Place, PlaceBranch, Address, Image, PlaceInfo, Service, PhoneNumber

admin.site.register(Place)
admin.site.register(PlaceBranch)
admin.site.register(Address)
admin.site.register(Image)
admin.site.register(PlaceInfo)
admin.site.register(Service)
admin.site.register(PhoneNumber)
