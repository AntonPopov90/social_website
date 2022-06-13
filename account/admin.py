from django.contrib import admin
from .models import Profile, BlogModel, CommentModel

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo', 'gender', 'relationship']


admin.site.register(Profile)
admin.site.register(BlogModel)
admin.site.register(CommentModel)