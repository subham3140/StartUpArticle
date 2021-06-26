from django.contrib import admin
from .models import Article, Interview, MediaArticle
# Register your model1s here.

admin.site.register(Article)
admin.site.register(MediaArticle)
admin.site.register(Interview)
