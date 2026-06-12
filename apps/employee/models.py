from django.db import models

class Identify(models.Model):
    identity = models.CharField(max_length=15, null=False, blank=False)
    post = models.BooleanField(default=True)

    def __str__(self):
        return self.identity