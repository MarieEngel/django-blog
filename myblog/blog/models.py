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
