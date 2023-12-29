from django.shortcuts import render
from .models import Gallery, Team, Content
from django.core.paginator import Paginator


def index(request):
    contents = Content.objects.all()
    return render(request, 'pages/index.html', {'contents': contents})


def about(request):
    teams = Team.objects.all()
    return render(request, 'pages/about.html',{'teams': teams})


def gallery(request):
    images = Gallery.objects.all()

    paginator = Paginator(images, 40)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/gallery.html', {'page_obj': page_obj})
