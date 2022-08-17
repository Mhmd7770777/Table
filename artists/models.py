from django.db import models

# Create your models here.
class Artists(models.Model):
    name = models.CharField(max_length=64, null=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Gender(models.Model):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Other"))

    artist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)

    def __str__(self):
        return self.gender


class Countries(models.Model):
    COUNTRY_CHOICES = (
        ("USA", "America"),
        ("Fr", "France"),
        ("UK", "United Kingdom"),
        ("Sp", "Spain"),
        ("Gr", "Germany"),
    )

    artist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    country = models.CharField(max_length=16, choices=COUNTRY_CHOICES)

    def __str__(self):
        return self.country
