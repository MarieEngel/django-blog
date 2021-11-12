from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=150)
    title_tag = models.CharField(max_length=150, default="Title")
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")


# class Image(models.Model):
#     title = models.CharField(max_length=200)
#     image = models.ImageField(upload_to="media/")

#     def __str__(self):
#         return self.title


# class Post(models.Model):
#     title = models.CharField(max_length=150)
#     body = models.TextField()
#     date = models.DateTimeField(auto_now=True)
#     content = models.TextField(default=None, blank=True)

#     def __str__(self):  # we create this function to be called
#         return self.title


# title
# body
# date
