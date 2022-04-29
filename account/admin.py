from django.contrib import admin
from .models import Profile, Statistic

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo', 'gender', 'relationship']


admin.site.register(Profile, ProfileAdmin)