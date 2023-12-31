from django.db import models


class Park(models.Model):
    name = models.CharField(
        'name',
        max_length=100,
        help_text='Maximum of 100 symbols',
        null=True,
        blank=True,
    )
    description = models.TextField(
        'description',
        max_length=1000,
        help_text='Maximum of 1000 symbols',
        null=True,
        blank=True,
    )
    address = models.CharField(
        'address',
        max_length=200,
        help_text='Maximum of 200 symbols',
        null=True,
        blank=True,
    )
    coordinates = models.CharField(
        'coordinates',
        max_length=100,
        help_text='Maximum of 100 symbols',
        null=True,
        blank=True,
    )
    email = models.EmailField(
        'email', help_text='Maximum of 254 symbols', null=True, blank=True
    )
    phone = models.CharField(
        'phone',
        max_length=15,
        help_text='Maximum of 15 symbols',
        null=True,
        blank=True,
    )
    website = models.CharField(
        'website',
        max_length=200,
        help_text='Maximum of 200 symbols',
        null=True,
        blank=True,
    )
    organization = models.CharField(
        'organization',
        max_length=200,
        help_text='Maximum of 200 symbols',
        null=True,
        blank=True,
    )
    inn = models.CharField(
        'inn',
        max_length=12,
        help_text='Maximum of 12 symbols',
        null=True,
        blank=True,
    )
