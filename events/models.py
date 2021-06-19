from django.db import models

# Create your models here.
class Event(models.Model):
    event_image = models.ImageField(upload_to='event_images/')
    enent_text = models.CharField(max_length=300)

    def __str__(self):
        return self.enent_text[:30]