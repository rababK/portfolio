from django.contrib import admin
from .models import basicInformation , blogArticle ,skill ,project , projectSkills
# Register your models here.
admin.site.register(basicInformation)
admin.site.register(blogArticle)
admin.site.register(skill)
admin.site.register(project)
admin.site.register(projectSkills)

