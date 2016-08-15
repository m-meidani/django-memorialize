from __future__ import unicode_literals

from django.db import models

import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('pic_folder/', filename)


# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    url = models.SlugField(unique=True, default=uuid.uuid1)
    is_url_valid = models.BooleanField(default=True)


class Message(models.Model):
    person = models.ForeignKey(Person)
    text_message = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=get_file_path, blank=True, null=True)


