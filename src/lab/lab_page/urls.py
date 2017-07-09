
from django.conf.urls import  include, url

from .views import(
    news,
    home,
    news_detail,
    news_create,
    news_delete,
    news_update,
    regions_list
   )



urlpatterns = [

    url(r'^$', home, name='home'),
    url(r'^news/$', news, name='news'),
    url(r'^create/$', news_create,),
    url(r'^regions/$', regions_list,),
    #urls for working width news (edit/delete/detail)

    url(r'^(?P<slug>[\w-]+)/$', news_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', news_update, name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$', news_delete, name='delete'),


    #url(r'^(regions/?P<slug>[\w-]+)/$', regions_list, name='regions'),

]


