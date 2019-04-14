from django.contrib import admin
from .models import Question,Choice,UserProfileInfo

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserProfileInfo)

# Register your models here.
