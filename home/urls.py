from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path,include
from .views import IndexView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'home'

urlpatterns = [
    path('', IndexView.as_view(),name ='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)