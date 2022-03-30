from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path,include
from .views import IndexView, StoryView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'home'

urlpatterns = [
    path('', IndexView.as_view(),name ='index'),
    path('story/',StoryView.as_view(),name="story")
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)