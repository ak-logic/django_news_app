from django.shortcuts import render, redirect
# from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from news.models import News, Profile
from django.contrib.auth import login, authenticate, logout, views
from django.conf import settings
from django.contrib.auth.decorators import login_required
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
            return redirect('/news/read/')
    else:
        form = SignUpForm()
    return render(request, 'news/signup.html', {'form': form})


@login_required(login_url='/news/login/', redirect_field_name='next')
def read_news(request):
    news_list = News.objects.all()
    context = {'news':news_list, 'page_name': 'All news'}
    return render(request, 'news/index.html', context)


@login_required(login_url='/news/login/', redirect_field_name='next')
def create_news(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    context = {'first_name': first_name, 'last_name': last_name}
    return render(request, 'news/create.html', context)

@login_required(login_url='/news/login/', redirect_field_name='next')
def delete_news(request, slug):
    article_to_delete = News.objects.get(slug=slug)
    article_to_delete.delete()
    return redirect('/news/read/')

@login_required(login_url='/news/login/', redirect_field_name='next')
def save_news(request):
    # try:
    if request.method == 'POST':
        new_article = News()
        writer = Profile.objects.get(user=request.user)
        new_article.title = request.POST['title']
        new_article.content = request.POST['news_content']
        new_article.writer = writer
        new_article.save()
    return redirect('/news/read/')
    # except Exception as error:
    # context = {'err_msg': error}
    # return render(request, 'news/index.html', context)

@login_required(login_url='/news/login/', redirect_field_name='next')
def edit_news(request, slug):
    article = News.objects.get(slug=slug)
    context = {'article': article, 'news_id': article.id}
    return render(request, 'news/edit.html', context)

@login_required(login_url='/news/login/', redirect_field_name='next')
def complete_edit(request):
    if request.method == 'POST':
        news_id = request.POST['news_id']
        article_edited = News.objects.get(id=news_id)
        article_edited.title = request.POST['title']
        article_edited.content = request.POST['news_content']
        article_edited.save()
    return redirect('/news/read/')

@login_required(login_url='/news/login/', redirect_field_name='next')
def my_news(request):
    all_news = News.objects.all()
    my_news = []
    for record in all_news:
        if record.writer.user == request.user:
            my_news.append(record)
    # news_list = News.objects.filter(writer_id=())
    context = {'news':my_news, 'page_name': 'My news'}
    return render(request, 'news/index.html', context)
