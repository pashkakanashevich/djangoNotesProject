from django.db import models

# Create your models here.
class Notes(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Below Normal'),
        (3, 'Normal'),
        (4, 'Above Normal'),
        (5, 'High'),
    ]

    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='notes_images/', blank=True, null=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Название: {self.title}'
