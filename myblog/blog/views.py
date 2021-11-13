from django.views.generic.edit import DeleteView
import git
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Blog
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import ListView, DetailView, CreateView
from .forms import BlogForm, ContactForm


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
    # fields = "__all__"  # fields and form_class can not be specified both


# class ContactView(CreateView):
#     model = Blog
#     template_name = "blog/contact.html"


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email_address"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, "admin@example.com", ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("main:homepage")

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
