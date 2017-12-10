from django.contrib import admin

from places.models import Place, PlaceBranch, Address, Image, PlaceInfo, Service


class MyModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Place, MyModelAdmin)
admin.site.register(PlaceBranch, MyModelAdmin)
admin.site.register(Address, MyModelAdmin)
admin.site.register(Image, MyModelAdmin)
admin.site.register(PlaceInfo, MyModelAdmin)
admin.site.register(Service, MyModelAdmin)
