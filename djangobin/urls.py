from django.urls import path, re_path
from . import views
 
app_name = "djangobin"

urlpatterns = [
	path('', views.index, name='index'),
	re_path('^trending/$', views.trending_snippets, name='trending_snippets'),
    re_path('^trending/(?P<language_slug>[\w]+)/$', views.trending_snippets, name='trending_snippets'),
    re_path('^(?P<snippet_slug>[\d]+)/$ ', views.snippet_detail, name='snippet_detail'),
    re_path('^tag/(?P<tag>[\w-]+)/$', views.tag_list, name='tag_list'),
    re_path('add-lang/', views.add_lang, name='add_lang')
    
]
