from django.contrib import admin
from .models import Article, Interview, MediaArticle, Content, InterViewContent
# Register your model1s here.

admin.site.register(Article)
admin.site.register(MediaArticle)
admin.site.register(Interview)
admin.site.register(Content)
admin.site.register(InterViewContent)
