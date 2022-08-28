from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Other"))

COUNTRY_CHOICES = (
    ("US", "America"),
    ("FR", "France"),
    ("UK", "United Kingdom"),
    ("ES", "Spain"),
    ("GE", "Germany"),
)


class Artist(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    age = models.IntegerField(null=True)
    name = models.CharField(max_length=64, null=True)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, null=True)
    country = models.CharField(max_length=16, choices=COUNTRY_CHOICES, null=True)

    def __str__(self):
        return self.name
