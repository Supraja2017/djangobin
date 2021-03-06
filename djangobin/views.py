from django.shortcuts import HttpResponse, render
from django.shortcuts import redirect
import datetime
from django import template
from django.conf import settings
from .forms import LanguageForm
from django.contrib import messages

def index(request):
	return HttpResponse("<p>Hello Django</p>")


def snippet_detail(request, snippet_slug):
    return HttpResponse('viewing snippet #{}'.format(snippet_slug))
 
 
def trending_snippets(request, language_slug=''):
    return HttpResponse("trending {} snippets".format(language_slug if language_slug else ""))
 
 
def tag_list(request, tag):
    return HttpResponse('viewing tag #{}'.format(tag))

def test_logged_on_or_not(request):
    if request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return redirect("login")

def add_lang(request):
    if request.POST:
        f = LanguageForm(request.POST)
        if f.is_valid():
            lang = f.save()
            messages.add_message(request, messages.INFO, 'Language saved.')	
            return redirect('djangobin:add_lang')
 
    else:
        f = LanguageForm()
 
    return render(request, 'djangobin/add_lang.html', {'form': f} )
