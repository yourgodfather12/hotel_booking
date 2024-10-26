from django.db import models

class Accommodation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name
