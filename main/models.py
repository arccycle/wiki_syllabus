from django.db import models

# Create your models here.
class Professor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 60)
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)

    def __str__(self):
        """Return the username of this account."""
        return self.username