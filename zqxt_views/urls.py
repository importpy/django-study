from django.conf.urls import include, url
from django.contrib import admin
from calc import views as calc_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/$',calc_views.add,name='add'),
    url(r'^add/(?P<a>\d+)/(?P<b>\d+)/$',calc_views.add2,name='add2'),
    url(r'^$',calc_views.index,name='home'),
    ]
