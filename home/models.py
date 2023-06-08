from django.db import models

# Create your models here.
import uuid
import os

class Folder(models.Model):
    uuid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)


def get_upload_path(instance, filename):
    return os.path.join(str(instance.folder.uuid), filename)

class File(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to='get_upload_path')
    created_at = models.DateTimeField(auto_now=True)
