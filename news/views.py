import re, random
from django.shortcuts import render, HttpResponseRedirect, HttpResponsePermanentRedirect, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, EmailMessage, send_mass_mail
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from news.models import News
from news.api import NewsResource
from django.contrib.auth.models import Permission
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth import views
from django.contrib.auth.tokens import PasswordResetTokenGenerator, default_token_generator
from tastypie.api import Api
from news.api import NewsResource, UserResource
from news.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/news/')
    else:
        form = SignUpForm()
    return render(request, 'news/signup.html', {'form': form})


@login_required(login_url='/login/', redirect_field_name='next')
def read_news(request):
    all_news_api = Api(api_name='v1')
    context = {'page_name': 'Home page', 'all_news_api': all_news_api}
    return render(request, 'news/index.html', context)
