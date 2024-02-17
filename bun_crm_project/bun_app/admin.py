from django.contrib import admin
from .models import CustomUser, Client, Commercial_offer, Advertising, AdvertisingCategory, Role

admin.site.register(Client)
admin.site.register(CustomUser)
admin.site.register(Commercial_offer)
admin.site.register(Advertising)
admin.site.register(AdvertisingCategory)
admin.site.register(Role)

