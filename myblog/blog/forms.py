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
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    subject = forms.CharField(max_length=50)
    email = forms.EmailField(
        max_length=150,
        required=True,
    )
    message = forms.CharField(widget=forms.Textarea, max_length=2000, required=True)
