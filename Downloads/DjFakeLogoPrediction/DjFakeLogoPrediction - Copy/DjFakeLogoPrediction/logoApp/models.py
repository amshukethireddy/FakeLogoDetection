from re import T
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    specialization = models.CharField(max_length=30, null=True, blank=True)
    experience = models.CharField(max_length=30, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username

MOTHER_RACE = ((1, 'Asian'),
               (2, 'Black or African American'),
               (3, 'Caucasian or White'),
               (4, 'Hispanic or Latino'),
               (5, 'Native American or Alaskan Native'),
               (6, 'Other'))

MARITAL_STATUS = ((0, 'No'), (1, 'Yes'))

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    input_file = models.FileField(null=True, blank=True)
    output_file = models.FileField(null=True, blank=True)
    max_prob = models.CharField(max_length=230, null=True, blank=True)
    prediction = models.CharField(max_length=230, null=True, blank=True)
    predict_class = models.CharField(max_length=230, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username