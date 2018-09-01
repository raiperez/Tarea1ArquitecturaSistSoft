from django.db import models

# Create your models here.
class Comment(models.Model):
    text = models.CharField(max_length=256)
    ip_address = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
