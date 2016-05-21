from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.project_list, name='project_list'),
    url(r'^handler/(?P<pk>\d+)/$', views.handler_projects, name='handler_projects'),
    url(r'^project/new/$', views.project_new, name='project_new')
]
