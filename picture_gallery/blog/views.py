from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator


def blogs(request):
    bloggings = Blog.objects.all()
    paginator = Paginator(bloggings, 15)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', {'page_obj': page_obj})


def blog_page(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/blog-single.html', {'blog': blog})
