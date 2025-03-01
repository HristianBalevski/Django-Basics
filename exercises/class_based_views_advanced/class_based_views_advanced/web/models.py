from django.db import models
from django.utils.text import slugify
import uuid


def get_random_hash():
    return uuid.uuid4().hex[-4:]


def generate_slug(*args, **kwargs):
    return get_random_hash()


class Todo(models.Model):
    MAX_TITLE_LENGTH = 24
    MAX_TENANT_LENGTH = 16

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        null=False,
        blank=False,
    )

    description = models.TextField()

    is_done = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        editable=False,

    )

    tenant = models.CharField(
        max_length=MAX_TENANT_LENGTH,
        null=True,
        blank=True,
        default=None
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) + get_random_hash()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title