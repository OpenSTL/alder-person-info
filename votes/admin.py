from django.contrib import admin

# Register your models here.

from .models import Vote, Ward

admin.site.register(Vote)
admin.site.register(Ward)