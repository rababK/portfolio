
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', include('portfolioCode.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += urlpatterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))
#static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)