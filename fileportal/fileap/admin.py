from django.contrib import admin
from .models import UploadedFile

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'filename', 'user', 'uploaded_at']
    list_filter = ['uploaded_at', 'user']
