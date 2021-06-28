from articleapp.models import Article
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Article, InterViewContent, Interview, MediaArticle
from django.core.serializers import serialize
import json

# Create your views here.

def home(request):
    return render(request, "base.html")

def allArticles(request):
    allarticles = Article.objects.all()
    toparticles = "empty"
    try:
      toparticles = allarticles[0]
      article = "Not empty"
    except:
      pass 
    context = {
        "allarticles": allarticles,
        "toparticle": toparticles
        }
    if request.is_ajax():  
      if request.GET.get("nav") == "interview" or request.GET.get("nav") == "article":
         selected_nav = [Article.objects.get(author=ins.author) for ins in Interview.objects.all()]  
      elif request.GET.get("nav") == "idea":   
         selected_nav = InterViewContent.objects.filter(content_type="idea") 
      else:  
        try: 
          selected_nav = [Article.objects.get(author=ins.author) for ins in InterViewContent.objects.filter(content_type=request.GET.get("nav"))]
        except:
          pass  
      data = serialize("json", selected_nav) 
      data = json.loads(data)
      return JsonResponse({"result":data})    
    return render(request, "articles.html", context)


def article(request, pk):
    article = Article.objects.get(id=pk) 
    interview = Interview.objects.get(author=article.author)
    context = {
      "pk": pk,
      "interview": interview,
      "article": article
    }
    return render(request, "interview.html", context) 
