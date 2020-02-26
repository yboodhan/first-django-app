from django.contrib import admin

# Register your models here. (admin can control)
from .models import Question

admin.site.register(Question)