from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.allArticles, name="allarticles"),
    path('article/<int:pk>', views.article, name="article"),
]