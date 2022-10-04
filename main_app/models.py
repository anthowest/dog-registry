from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=2000)
    bio = models.TextField(max_length=2000)
    hypoallergenic = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Health(models.Model):
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    life_expectancy = models.IntegerField(default=0)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="health")

    def __str__(self):
        return self.title