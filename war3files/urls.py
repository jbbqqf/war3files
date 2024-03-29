"""war3files URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from units.views import RaceListView, race_detail_view, UnitDetailView

urlpatterns = [
    url(r'^$', RaceListView.as_view()),
    url(r'^race/(?P<slug>[-\w]+)/?$', race_detail_view),
    url(r'^unit/(?P<slug>[-\w]+)/?$', UnitDetailView.as_view()),

    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
