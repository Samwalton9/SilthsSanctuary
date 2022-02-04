from django.db import models

from SilthsSanctuary.adverts.models import Advert


class Animal(models.Model):

    name = models.CharField(help_text="Internal name of this animal.")
    adopted_name = models.CharField(
        null=True,
        blank=True,
        help_text="Name of animal post-adoption."
    )

    date_of_birth = models.DateField(help_text="Estimate if unknown.")

    breed = models.CharField(null=True, blank=True)

    # TODO: FK to Adopter, when that model is operational
    # adopter = models.ForeignKey

    # Species selection
    SPECIES_CHOICES = [
        ('Cat', 'Cat'),
        ('Gerbil', 'Gerbil')
    ]

    species = models.CharField(
        choices=SPECIES_CHOICES
    )

    microchip_number = models.CharField(
        null=True,
        blank=True,
    )

    advert = models.ForeignKey(
        Advert,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )


class CatsMedical(models.Model):

    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)

    last_deflead = models.DateField(
        null=True,
        blank=True,
        help_text="Date the animal was last deflead"
    )

    last_dewormed = models.DateField(
        null=True,
        blank=True,
        help_text="Date the animal was last dewormed"
    )
