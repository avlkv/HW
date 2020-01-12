"""lab5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from my_app.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin_url'),
    url(r'^$', RedirectView.as_view(url='/main/', permanent=False), name='index'),
    url(r'^main/$', main, name='main_url'),
    url(r'^db/$', db, name='db_url'),
    url(r'^books/$', books, name='books_url'),
    url(r'^reader/$', ReaderView.as_view(), name='reader_url'),
    url(r'^registration/$', registration, name='registration_url'),
    url(r'^registration2/$', registration2, name='registration2_url'),
    url(r'^login/$', login, name='login_url'),
    url(r'^success/$', success, name='success_url'),
    url(r'^logout/$', logout, name='logout_url'),
    url(r'^list_books/(?P<id>\d+)', book_id, name='book_id_url'),
    url(r'^list_books/', ListBookView, name='list_books_url'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
