from django.views.generic.edit import DeleteView
import git
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Blog
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import ListView, DetailView, CreateView
from .forms import BlogForm


class HomeView(ListView):
    model = Blog
    template_name = "blog/home.html"
    context_object_name = "blog_posts"


class BlogPostView(DetailView):
    model = Blog
    template_name = "blog/blog_post.html"


class AddPostView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/add_blogpost.html"
    fields = "__all__"


@csrf_exempt
def update(request):
    if request.method == "POST":
        """
        pass the path of the directory where your project will be
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "mariee.pythonanywhere.com/"
        """
        repo = git.Repo("~/django-blog")
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere, you can trust")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere, sorry")
