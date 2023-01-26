from django.contrib import admin
from django.urls import path
from home import views
from home.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path("", IndexView.as_view(), name='index'),
                  path("contact/", Contact.as_view(), name='contact'),
                  path("history/", History.as_view(), name='history'),
                  path("about/", AboutMe.as_view(), name='AboutMe'),
                  path("achievement/", Achievement.as_view(), name='Achievements'),
                  path("projects/", Project.as_view(), name='Projects'),
                  # path("csbridgeprogram/", CsBrideProgram.as_view(), name='CsBridgeProgram'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
