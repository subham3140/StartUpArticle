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
    image = models.ImageField(upload_to="interview Image", null = True)
    video = models.FileField(upload_to="video/%y", null=True)

class Article(models.Model):
    title = models.TextField(null=False, blank=False)
    author =  models.CharField(max_length=500, null=False)
    profile = models.ImageField(upload_to="profile", null=True)
    interview = models.ForeignKey(to=Interview, on_delete=models.CASCADE)

