from django.contrib import admin
from .models import Expense
# Register your models here.

@admin.register(Expense)
class Expens_admin(admin.ModelAdmin):
    list_display = ['text','amount','date','user']
    TimeField = ('date',)
    search_fields = ['amount']