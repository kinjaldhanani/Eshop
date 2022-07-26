from django.contrib.auth.models import AbstractUser, User, UserManager
from django.db import models


class User(AbstractUser):
    GENDER_MALE = "m"
    GENDER_FEMALE = "f"
    OTHER = "o"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (OTHER, "Other"),
    )
    objects = UserManager()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to="images/", null=True, blank=True)
    phone_number = models.IntegerField(null=True, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username


