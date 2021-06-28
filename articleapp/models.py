from django.db import models
from django.utils import tree

# Create your models here.

CONTENT_TYPE = (
    ("question", "Question"),
    ("answers", "Answers"),
    ("inspiration", "Inspiration"),
    ("success_key", "Success Key"),
    ("story", "story"),
    ("idea", "Idea"),
    ("achievement", "Achievement"),
    ("influencer", "Influencer"),
    ("contact", "Contact"),
    ("goal", "Goal"),
)

GENDER = (
    ("male", "Male Avatar"),
    ("female", "Female Avatar")
)

class MediaArticle(models.Model):
    image = models.ImageField(upload_to="interview_image")
    video = models.FileField(upload_to="video/%y", null=True, blank=True)
    author =  models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "media field of {}".format(self.author)   
        
class InterViewContent(models.Model):
    author =  models.CharField(max_length=500, null=True, blank=True)
    content = models.TextField(null=True)
    content_type = models.CharField(choices=CONTENT_TYPE, max_length=200, default= "question")
    media = models.ManyToManyField(to=MediaArticle)
    gender = models.CharField(choices=GENDER, max_length=400, default="male")

    def __str__(self):
        return "{} for {}".format(self.content_type,self.author)

class Interview(models.Model):
    heading = models.TextField(null=False)
    contents = models.ManyToManyField(to=InterViewContent)
    author =  models.CharField(max_length=500, null=True, blank=True)
    about = models.TextField(null=False, default="")
    
    def __str__(self):
        return f'interview of {self.author}'


class Article(models.Model):
    title = models.TextField(null=False, blank=False)
    profile = models.ImageField(upload_to="profile", null=True, blank=True)
    interview = models.ForeignKey(to=Interview, on_delete=models.CASCADE, null=True)
    author =  models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'article of {self.author}'



# for each paragraph - @changepg
# for each ending question - @qend
# for each ending answer - @ansend
# for list items - @changel