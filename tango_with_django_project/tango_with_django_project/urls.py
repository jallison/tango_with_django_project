"""
Definition of urls for tango_with_django_project.
"""

from django.conf.urls import include, url
from rango import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', tango_with_django_project.views.home, name='home'),
    # url(r'^tango_with_django_project/', include('tango_with_django_project.tango_with_django_project.urls')),
    url(r'^rango/', include('rango.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    

]
