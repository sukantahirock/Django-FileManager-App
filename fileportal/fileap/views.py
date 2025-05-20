# fileapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, FileUploadForm
from .models import UploadedFile
from django.http import FileResponse, HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import os
from django.contrib.admin.views.decorators import staff_member_required
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Send email
            send_mail(
                subject='Welcome to FilePortal!',
                message='Thank you for registering.',
                from_email='noreply@fileportal.com',
                recipient_list=[user.email],
            )
            return redirect('file-list')
    else:
        form = RegisterForm()
    return render(request, 'fileap/register.html', {'form': form})

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded = form.save(commit=False)
            uploaded.user = request.user
            uploaded.save()
            return redirect('file-list')
    else:
        form = FileUploadForm()
    return render(request, 'fileap/upload.html', {'form': form})

@login_required
def file_list(request):
    files = UploadedFile.objects.all() if request.user.is_staff else UploadedFile.objects.filter(user=request.user)
    return render(request, 'fileap/list.html', {'files': files})

@login_required
def download_file(request, file_id):
    obj = get_object_or_404(UploadedFile, id=file_id)
    if obj.user == request.user or request.user.is_staff:
        return FileResponse(open(os.path.join(settings.MEDIA_ROOT, obj.file.name), 'rb'), as_attachment=True)
    return HttpResponse("Unauthorized", status=401)

@login_required
def delete_file(request, file_id):
    obj = get_object_or_404(UploadedFile, id=file_id)
    if obj.user == request.user or request.user.is_staff:
        obj.file.delete()
        obj.delete()
        return redirect('file-list')
    return HttpResponse("Unauthorized", status=401)


@staff_member_required
def admin_panel(request):
    files = UploadedFile.objects.all()
    return render(request, 'fileap/admin_panel.html', {'files': files})
