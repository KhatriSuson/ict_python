from django.contrib import admin
from . models import Level, Challenge, UserProgress
# Register your models here.
admin.site.register(Level)
admin.site.register(Challenge)
admin.site.register(UserProgress)