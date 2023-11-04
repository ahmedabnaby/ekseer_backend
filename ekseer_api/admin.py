from django.contrib import admin
from .models import CustomUser, Call,Consultation, Rating

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Call)
admin.site.register(Consultation)
admin.site.register(Rating)

