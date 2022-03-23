import git
import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import ListView, DetailView, CreateView
from .forms import BlogForm, ContactForm
from myblog.settings import EMAIL_HOST_USER


class HomeView(ListView):
    model = Blog
    template_name = "blog/home.html"
    context_object_name = "blog_posts"


class BlogPostView(DetailView):
    model = Blog
    template_name = "blog/blog_post.html"

logger = logging.getLogger("add_post_logger")
class AddPostView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/add_blogpost.html"


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            message = f"""
            from: {cleaned["name"]} {cleaned["email"]}
            {cleaned["message"]}
            """
            try:
                send_mail(
                    cleaned["subject"],
                    message,
                    EMAIL_HOST_USER,
                    [EMAIL_HOST_USER],
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("home")

    form = ContactForm()
    return render(request, "blog/contact.html", {"form": form})


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
