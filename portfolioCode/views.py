from django.shortcuts import render, redirect
from . import models
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
          

            try:
                send_mail(
                    f'From {name}, Subject: {" from client "}',
                    f' the email : {email} \n Message: {message}',
                    email,
                    [settings.ADMIN_EMAIL],  # To email
                    fail_silently=False,
                )
               
                return redirect('index')
            except Exception as e:
                print("Error sending email:", e)
                return HttpResponse(f"Failed to send email: {e}")
        else:
            # Return the form with errors back to the template
            return render(request, 'portfolioCode/index.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'portfolioCode/index.html', {'form': form})


