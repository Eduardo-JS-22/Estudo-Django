from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Image(models.Model):
    CATEGORY_OPTIONS = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta')
    ]

    name = models.CharField(max_length=255, null=False, blank=False)
    legend = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_OPTIONS, default='')
    description = models.TextField()
    photo = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    published = models.BooleanField(default=False)
    image_date = models.DateTimeField(default=datetime.now, blank=False)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user')

    def __str__(self):
        return self.name