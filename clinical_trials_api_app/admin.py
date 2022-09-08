from django.contrib import admin
from .models import StudyItem

# Access study from admin panel
admin.site.register(StudyItem)
