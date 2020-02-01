from django.contrib import admin
from .models import *


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','email','specialization','date_added')
    list_filter = ('name',)
    search_fields = ('email','specialization')

    # def name(self, obj):
    #     return obj.name or f'Empty sku, ID: {obj.id}'
    # name.description = 'SKU'

    # def get_ordering(self, request):
    #     if request.user.is_superuser:
    #         return ('name','email')
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','date_added')
    list_filter = ('name',)
    search_fields = ('email','name')

admin.site.register(Portfolio)
admin.site.register(SignUp)
admin.site.register(Team,TeamAdmin)
admin.site.register(Contact,ContactAdmin)

# Register your models here.
