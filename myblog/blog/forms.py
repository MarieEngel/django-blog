from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "title_tag", "body", "header_image")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
            # "header_image": form.TextInput(attrs={"class": "form-control"}),
            # "date": form.TextInput(attrs={"class": "form-control"}),
        }
