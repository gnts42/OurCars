#from django.conf.urls import include, url
from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^ourcarsapp/', include('ourcarsapp.urls')),
    re_path(r'^', include('ourcarsapp.urls')),
  #  url(r'^stocks/', views.Stocklist.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)