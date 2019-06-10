from django.db import models
from datetime import datetime
# Create your models here.


class FileUpload(models.Model):
    name = models.CharField(max_length=200, verbose_name="file_name")
    file = models.FileField(upload_to="file/resource/%Y/%m", verbose_name=u"file_address", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add_time")

    class Meta:
        verbose_name = u"file_resource"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)


class ImageUpload(models.Model):
    name = models.CharField(max_length=200, verbose_name="image_name")
    image = models.FileField(upload_to="image/resource/%Y/%m", verbose_name=u"image_address", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add_time")

    class Meta:
        verbose_name = u"image_resource"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

