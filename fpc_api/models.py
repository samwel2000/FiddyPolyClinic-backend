from django.db import models
from PIL import Image
import os
from uuid import uuid4
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# HELPER FUNCTION FOR FILE NAMES AND IMAGE NAMES


def get_file_name(instance, filename):
    extension = os.path.splitext(filename)[1].lower()
    new_name = f'{uuid4()}{extension}'
    return os.path.join(instance.string_directory_var, new_name)


class News(models.Model):
    heading = models.CharField(max_length=500)
    string_directory_var = 'news'
    photo = models.ImageField(upload_to=get_file_name)
    image_info = models.CharField(max_length=500)
    news_content = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.heading[:100]

    class Meta:
        verbose_name_plural = "News"
        ordering = ['-pk']


class Jobs(models.Model):
    string_directory_var = 'jobs'
    title = models.CharField(max_length=500)
    position_number = models.PositiveBigIntegerField()
    content = models.TextField()
    qualifications = models.TextField(
        blank=True, null=True, help_text="Enter qualifications separated by a comma after each qualification")
    filefield = models.FileField(upload_to=get_file_name, storage=RawMediaCloudinaryStorage())
    created_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title[:100]

    class Meta:
        verbose_name_plural = "Jobs"
        ordering = ['-pk']


class TeamMembers(models.Model):
    string_directory_var = 'teamMembers'
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to=get_file_name)
    position = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        super(TeamMembers, self).save(*args, **kwargs)
        image = Image.open(self.photo.path)
        if image.width > 300 or image.height > 300:
            output_size = (200, 200)
            image.thumbnail(output_size)
            image.save(self.photo.path)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = "Team Members"


class ContactUs(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.email

    class Meta:
        verbose_name_plural = "User messages"
        ordering = ['-pk']
