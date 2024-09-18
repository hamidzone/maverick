from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=255)
    price=models.FloatField()
    description=models.TextField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5