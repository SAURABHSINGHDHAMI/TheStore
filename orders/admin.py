from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress

# Register your models here.

admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "user", "createdAt", "totalPrice"
    ]