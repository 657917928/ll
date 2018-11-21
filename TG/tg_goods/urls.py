
from django.conf.urls import url
from  tg_goods import views
urlpatterns=[
    url(r'^$',views.index),

    url(r'^list(\d+)_(\d+)_(\d+)/$',views.goodlist),
    url(r'^(\d+)/$', views.detail),
]