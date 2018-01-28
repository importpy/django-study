from django.conf.urls import include, url
from django.contrib import admin
from learn import views as learn_views # new

urlpatterns = [
    url(r'^$', learn_views.index), #new
    url(r'^admin/', include(admin.site.urls)),
    
]
