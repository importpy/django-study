from django.conf.urls import include, url
from django.contrib import admin
from learn import views as learn_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',learn_views.home,name='home'),
    url(r'^zifu$',learn_views.strtel,name='zifu'),
    url(r'^list$',learn_views.listtel,name='list'),
    url(r'^dict$',learn_views.dicttel,name='dict'),
    ]
