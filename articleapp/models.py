from django.db import models

# Create your models here.

CONTENT_TYPE = (
    ("question", "Question"),
    ("advise", "Advise"),
    ("achievement", "Achievement"),
    ("success_key", "Success Key"),
    ("contact", "Contact"),
    ("goal", "Goal"),
    ("other", "Other"),
    ("tips", "Tips")
)

class Interview(models.Model):
    heading = models.TextField(null=False)
    content = models.TextField(null=False, blank=False)
    content_type = models.CharField(choices=CONTENT_TYPE, max_length=200)
    author =  models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return f'interview of {self.author}'

class MediaArticle(models.Model):
    image = models.ImageField(upload_to="interview Image", null = True, blank=True)
    video = models.FileField(upload_to="video/%y", null=True, blank=True)

class Article(models.Model):
    title = models.TextField(null=False, blank=False)
    about = models.TextField(null=False, default="")
    author =  models.CharField(max_length=500, null=False)
    profile = models.ImageField(upload_to="profile", null=True, blank=True)
    interview = models.ManyToManyField(to=Interview)

    def __str__(self):
        return f'article of {self.author}'

