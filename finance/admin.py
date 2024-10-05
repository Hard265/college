from django.contrib import admin

from .models import Fee, Payment


class FeeAdmin(admin.ModelAdmin):
    list_display = ("name", "amount", "due_date", "description")


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "fee", "amount_paid", "payment_date")


admin.site.register(Fee, FeeAdmin)
admin.site.register(Payment, PaymentAdmin)
