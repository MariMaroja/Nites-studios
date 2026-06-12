from django.db import models

class Characters(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    game = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Videos(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    video = models.FileField(upload_to='video/%Y/%m/%d', null=False, blank=False)
    thumb = models.FileField(upload_to="thumbnail/%Y/%m/%d", blank=True)
    narration = models.TextField(null=False, blank=False)
    posted = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Synopsis(models.Model):
    text = models.TextField(null=False, blank=False)
    games = models.CharField(max_length=100, null=False, blank=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    reveal = models.BooleanField(default=True)

    def __str__(self):
        return self.text