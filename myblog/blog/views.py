from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Blog

# Create your views here.


def home(request):
    blog_posts = Blog.objects.all()
    blog_list_html = ""
    for blog in blog_posts:
        blog_list_html += f"<p><a href='/blog/{blog.id}/'>{blog.title}</a></p>"
    html = f"<html><body>{blog_list_html}</body></html>"
    return HttpResponse(html)


def blog_post(request, id=1):
    blog_post = Blog.objects.get(id=id)
    html = f"<html><body><h1>{blog_post.title}</h1>{blog_post.date}<p>{blog_post.body}</p></body></html>"
    return HttpResponse(html)


def index(request):
    blog_post_list = Blog.objects.order_by("-pub_date")[:5]
    template = loader.get_template("blog/index.html")
    context = {
        "blog_post_list": blog_post_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, blog_post_id):
    blog_post = get_object_or_404(Blog, pk=blog_post_id)
    return render(request, "blog/detail.html", {"blog_post": blog_post})
