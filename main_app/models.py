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