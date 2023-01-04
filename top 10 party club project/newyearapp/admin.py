from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import RegisterModel,ProductModel,BookingModel

# Register your models here.


@admin.register(RegisterModel)
class RegisterModelAdmin(admin.ModelAdmin):
    list_display =['id','username','email','password']


admin.site.register(ProductModel)


@admin.register(BookingModel)
class BookingModelAdmin(admin.ModelAdmin):
    list_display =['id','name','email','phone','person','msg']


