from django.db import models
from django.template.defaultfilters import slugify


class Pet(models.Model):
    name = models.CharField(max_length=30)
    personal_photo = models.URLField()
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=False, blank=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Pet.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
