from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class basicInformation(models.Model):
    logo=models.CharField(max_length=50,default="rabab KH.")
    aboutme=models.TextField()
    cvurl=models.CharField(max_length=150)

    whatsappNo=models.IntegerField()
    whatsappLink=models.CharField(max_length=150)

    telegramName=models.CharField(max_length=50)
    telegramLink=models.CharField(max_length=150)

    githubName=models.CharField(max_length=150)
    githubLink=models.CharField(max_length=150)

    linkedInName=models.CharField(max_length=150)
    linkedInlink=models.CharField(max_length=150)

    def __str__(self):
        return self.logo
    

class blogArticle(models.Model):
    title=models.CharField(max_length=250)
    article=models.TextField()
    def partOfarticle(self):
        return self.article[0:100]
    
    def __str__(self):
        return self.title
    

class skill(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class project(models.Model):

    title=models.CharField(max_length=250)
    about=models.TextField()
    
    
    def partOfabout(self):
        return self.about[0:100]
    def __str__(self):
        return self.title
    

class projectSkills(models.Model):
    skill = models.ForeignKey(skill, on_delete=models.CASCADE)
    project = models.ForeignKey(project, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill.name
    


