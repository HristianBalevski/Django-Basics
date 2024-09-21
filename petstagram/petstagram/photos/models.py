from django.db import models
from django.core.validators import MinLengthValidator

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_image_size


class Photo(models.Model):
    photo = models.ImageField(validators=(validate_image_size,))
    description = models.TextField(max_length=300, validators=[MinLengthValidator(10)])
    location = models.CharField(max_length=30)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)


class Comment(models.Model):
    comment = models.TextField(max_length=300)
    date_of_publication = models.DateField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
