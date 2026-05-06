from django.db import models

# Create your models here.


class MainSpec(models.Model):

    name = models.CharField(max_length = 255)  # Name of the phones (brand)
    property = models.CharField(max_length = 255)   # Technical characteristic
                                                    # (description) of the phone

    def __str__(self):
        return self.name