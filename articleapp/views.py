from articleapp.models import Article
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Article

# Create your views here.

def home(request):
    return render(request, "base.html")


def allArticles(request):
    allarticles = Article.objects.all()
    context = {
        "allarticles": allarticles,
        "toparticle": allarticles[0]
        }
    return render(request, "articles.html", context)