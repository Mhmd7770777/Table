from django.db import models

# Create your models here.


class Gender(models.Model):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Other"))

    option = models.CharField(max_length=7, choices=GENDER_CHOICES)

    def __str__(self):
        return self.option


class Country(models.Model):
    COUNTRY_CHOICES = (
        ("US", "America"),
        ("FR", "France"),
        ("UK", "United Kingdom"),
        ("ES", "Spain"),
        ("GE", "Germany"),
    )

    name = models.CharField(max_length=16, choices=COUNTRY_CHOICES)

    def __str__(self):
        return self.name


class Artist(models.Model):
    age = models.IntegerField(null=True)
    name = models.CharField(max_length=64, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
