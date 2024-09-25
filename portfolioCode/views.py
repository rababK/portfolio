from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    basicInfo = models.basicInformation
    basicInfo = basicInfo.objects.get(id=1)
     

    blogArticle = models.blogArticle
    blogArticles=blogArticle.objects.all()[:3]

    project = models.project
    projects = project.objects.all()[:6]


    context = {
        "basicInfo": basicInfo,
        "blogArticles":blogArticles,
        "projects":projects,
    

    }
    return render(request ,"portfolioCode/index.html",context)

def blogDetails(request,id):
    blogArticle = models.blogArticle
    article = blogArticle.objects.get(id=id)
    articles = blogArticle.objects.all()
    context = {
        "article": article,
        "articles": articles,
       
    

    }
    return render(request ,"portfolioCode/blog.html",context)


def projectDetails(request,id):
    Project = models.project
    projectSkills= models.projectSkills

    theproject = Project.objects.get(id=id)
    projects = Project.objects.all()

    skills=projectSkills.objects.filter(project=theproject.id)
    context = {
        "project": theproject,
        "projects":projects,
        "skills":skills
    

    }
    return render(request ,"portfolioCode/projects.html",context)


