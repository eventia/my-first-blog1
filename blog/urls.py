from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^branch1/$', views.branch1, name='branch1'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

]
