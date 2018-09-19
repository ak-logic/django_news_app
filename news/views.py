import re, random
from django.shortcuts import render, HttpResponseRedirect, HttpResponsePermanentRedirect, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from news.models import News, Profile
from django.contrib.auth import login, authenticate, logout, views
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordChangeForm, PasswordResetForm
from tastypie.api import Api
from news.api import NewsResource, UserResource
from news.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            newly_created_profile = Profile(user=user)
            # newly_created_profile.user = user
            newly_created_profile.bio = form.cleaned_data.get('bio')
            newly_created_profile.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/news/')
    else:
        form = SignUpForm()
    return render(request, 'news/signup.html', {'form': form})


@login_required(login_url='/login/', redirect_field_name='next')
def read_news(request):
    news_list = News.objects.all()
    context = {'news':news_list}
    return render(request, 'news/index.html', context)


@login_required(login_url='/login/', redirect_field_name='next')
def create_news(request):
    context = {}
    return render(request, 'news/create.html', context)

@login_required(login_url='/login/', redirect_field_name='next')
def delete_news(request, slug):
    news_to_delete = News.objects.get(slug=slug)
    news_to_delete.delete()
    return redirect('/news/')

@login_required(login_url='/login/', redirect_field_name='next')
def save_news(request):
    if request.method == 'POST':
        new_article = News()
        writer = Profile.objects.get(user=request.user)
        new_article.title = request.POST['title']
        new_article.content = request.POST['news_content']
        new_article.writer = writer
        new_article.save()
    return redirect('/news/')
