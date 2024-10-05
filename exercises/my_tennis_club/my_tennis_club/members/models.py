from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    slug = models.SlugField(default="", null=False, blank=True)  # Позволяваме празен slug

    def save(self, *args, **kwargs):
        # Ако slug е празно, генерираме го автоматично
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(f"{self.first_name} {self.last_name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"