from django.contrib import admin
from contact import models


@admin.register(models)
class ContactAdmin(admin.ModelAdmin):
    ...
