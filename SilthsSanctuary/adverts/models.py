from django.db import models


class Advert(models.Model):

    description = models.TextField()

    # TODO: Need to define where these are stored, and figure out the best method of having multiple files.
    # images = models.FileField()

    reserved = models.BooleanField(
        default=False,
        help_text="Has this animal been reserved by an adopter?"
    )
