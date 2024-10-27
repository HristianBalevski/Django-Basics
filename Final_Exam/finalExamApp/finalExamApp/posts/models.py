from django.core.validators import MinLengthValidator
from django.db import models

MIN_LENGTH_VALIDATOR = 5
MAX_LENGTH_VALIDATOR = 50


class Post(models.Model):
    title = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=MAX_LENGTH_VALIDATOR,
        validators=[MinLengthValidator(MIN_LENGTH_VALIDATOR), ],
        error_messages={
            'unique': "Oops! That title is already taken. How about something fresh and fun?"
        }
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        help_text="Share your funniest furry photo URL!"
    )

    content = models.TextField(
        blank=False,
        null=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        null=False
    )

    author = models.ForeignKey(
        'author.Author',
        on_delete=models.CASCADE,
        related_name='posts',
        null=False,
        editable=False
    )

    def __str__(self):
        return self.title
