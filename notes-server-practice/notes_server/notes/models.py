from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Название: {self.title}'
