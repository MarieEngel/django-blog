from django.views.generic.edit import DeleteView
import git
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Blog
from django.views.decorators.csrf import csrf_exempt

# from django.views.generic import ListView, DeleteView


def home(request):
    blog_posts = Blog.objects.all()
    context = {"blog_posts": blog_posts}
    return render(request, "blog/home.html", context)


# class HomeView(ListView):
#     model = Blog
#     template_name = "home.html"

# class BlogPostView(DeleteView):
#     model = Blog
#     template_name = "blog_post.html"


def blog_post(request, id=1):
    blog = Blog.objects.get(id=id)
    context = {"blog": blog}
    return render(request, "blog/blog_post.html", context)


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
