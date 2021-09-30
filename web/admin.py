from django.contrib import admin
from .models import Expense, income
# Register your models here.

@admin.register(Expense)
class Expens_admin(admin.ModelAdmin):
    list_display = ['text','amount','date','user']
    TimeField = ('date',)
    search_fields = ['amount']

@admin.register(income)
class income_admin(admin.ModelAdmin):
    list_display = ['text','amount','date','user']
    TimeField = ('date',)
    search_fields = ['amount']