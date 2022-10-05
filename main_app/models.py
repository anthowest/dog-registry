from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=2000)
    bio = models.TextField(max_length=2000)
    hypoallergenic = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class History(models.Model):
    nationality = models.CharField(max_length=30)
    year_recognized = models.IntegerField(default=0)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="historys")

    def __str__(self):
        return self.nationality

class Size(models.Model):
    size = models.CharField(max_length=10)
    dogs = models.ManyToManyField(Dog)

    def __str__(self):
        return self.size