from django.shortcuts import HttpResponse, render
from django.shortcuts import redirect
import datetime
from django import template
from django.conf import settings


def index(request):
	return HttpResponse("<p>Hello Django</p>")


def snippet_detail(request, snippet_slug):
    return HttpResponse('viewing snippet #{}'.format(snippet_slug))
 
 
def trending_snippets(request, language_slug=''):
    return HttpResponse("trending {} snippets".format(language_slug if language_slug else ""))
 
 
def tag_list(request, tag):
    return HttpResponse('viewing tag #{}'.format(tag))
