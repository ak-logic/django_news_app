from django.shortcuts import render, redirect

def landing_page(request):
    return render(request, 'django_news_app/landing_page.html')
