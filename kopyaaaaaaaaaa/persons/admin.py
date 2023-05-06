from django.contrib import admin

# # Register your models here.
from .models import BasimYili,YayinEvi,Sinif,KitapTuru,DersTuru,Kitap,Kitapismi
# ,KitapTuru,DersTuru,Kitap

admin.site.register(BasimYili)
admin.site.register(YayinEvi)
admin.site.register(Sinif)
admin.site.register(KitapTuru)
admin.site.register(DersTuru)
admin.site.register(Kitap)
admin.site.register(Kitapismi)