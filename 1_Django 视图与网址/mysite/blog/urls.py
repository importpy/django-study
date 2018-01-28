from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<post>[a-z]+)/$',views.post_detail,name='post_detail'),
    url(r'^$',views.post_list, name='post_list'),

    ]

