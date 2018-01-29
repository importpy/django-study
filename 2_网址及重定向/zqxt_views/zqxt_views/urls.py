from django.conf.urls import url
from django.contrib import admin
from calc import views as calc_views

urlpatterns = [
#    url(r'^add/$', calc_views.add, name='add'),
    url(r'^admin/', admin.site.urls),
    url(r'^add/(\d+)/(\d+)', calc_views.add2,name='add2'),
    url(r'^$',calc_views.index, name='home'),

    ]

