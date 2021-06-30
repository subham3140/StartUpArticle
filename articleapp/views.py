from articleapp.models import Article
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Article, InterViewContent, Interview
from django.core.serializers import serialize
from django.db.models import Q
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
    about = [item for item in interview.about.split("@nextpg")]
    questions = []
    answers = []
    listquestions = []
    listanswers = []
    for i in interview.contents.all():
      if i.content_type == "list question answer":
        split_qstn_ans = i.content.split("@nextq")
        listquestions.append(split_qstn_ans[0])
        listanswers.append(split_qstn_ans[1].split("@nextl"))
      else:
        split_qstn_ans = i.content.split("@nextq")
        questions +=split_qstn_ans[:-1]
        answers +=split_qstn_ans[-1].split("@nextan")
      
    normalQformat = {}   
    listQformat = {}
    for i in range(0, len(questions)):
      normalQformat[questions[i]] = answers[i] 
    for i in range(0, len(listquestions)):
          listQformat[listquestions[i]] = listanswers[i] 
    context = {
      "pk": pk,
      "interview": interview,
      "article": article,  
      "about": about,
      "normalQformat": normalQformat,
      "listQformat": listQformat
    }
    return render(request, "interview.html", context) 


def searched_articles(request):
  if request.is_ajax():  
      searched_text = request.GET.get("searched")
      allarticles = Article.objects.filter(Q(title__icontains=searched_text)|Q(author__icontains=searched_text))
      data = serialize("json", allarticles) 
      data = json.loads(data)
  return JsonResponse({"result": data})