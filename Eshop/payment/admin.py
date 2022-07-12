from django.contrib import admin
from payment.models import Payment


@admin.register(Payment)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'customer', 'amount', 'date']
