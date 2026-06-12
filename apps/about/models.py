from django.db import models

class AboutUs(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    profile = models.ImageField(upload_to="profiles/%Y/%m/%d/", blank=True)
    text = models.TextField(null=False, blank=False)
    role = models.CharField(max_length=100, null=False, blank=False)
    posted = models.BooleanField(default=True)

    def __str__(self):
        return self.name
