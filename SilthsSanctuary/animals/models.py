from django.db import models


class Animal(models.Model):

    name = models.CharField(help_text="Internal name of this animal.")
    adopted_name = models.CharField(
        null=True,
        blank=True,
        help_text="Name of animal post-adoption."
    )

    date_of_birth = models.DateField(help_text="Estimate if unknown.")

    breed = models.CharField(null=True, blank=True)

    # adopter = models.ForeignKey # FK to Adopter

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
        'adverts.advert',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )


class CatsMedical(models.Model):

    # We shouldn't be deleting medical records for animals without
    # deleting the animal, so use models.PROTECT to prevent
    # deletion of individual medical records.
    animal = models.ForeignKey('Animal', on_delete=models.PROTECT)

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
