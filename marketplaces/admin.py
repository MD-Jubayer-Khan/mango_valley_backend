from django.contrib import admin
from .models import Mango, Order

class MangoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'quantity')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'mango', 'status', 'order_date')

admin.site.register(Mango, MangoAdmin)
admin.site.register(Order, OrderAdmin)