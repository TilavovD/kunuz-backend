from django.core.files.uploadedfile import UploadedFile
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
from helpers.models import BaseModel


class Audio(BaseModel):
    title = models.CharField(max_length=128)
    track = models.FileField(upload_to='audio/')
    image = models.ImageField(upload_to='audio/image/')
    duration = models.PositiveIntegerField("audio duration in seconds", blank=True, null=True)

    def __str__(self):
        return self.title


import mutagen

@receiver(pre_save, sender=Audio)
def some_pre_save_receiver(sender, instance, raw, using, update_fields, **kwargs):
    file_was_updated = False
    if hasattr(instance.track, 'file') and isinstance(instance.track.file, UploadedFile):
        file_was_updated = True

    if update_fields and "track" in update_fields:
        file_was_updated = True

    if file_was_updated:
        # read audio file metadata
        audio_info = mutagen.File(instance.track).info
        # set audio duration in seconds, so we can access it in database
        instance.duration = int(audio_info.length)
