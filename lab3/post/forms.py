from django.forms import ModelForm
from django import forms
from post.models import Post

class PostForm(ModelForm):
    title = forms.CharField(max_length=63, widget=forms.TextInput(attrs={'class': 'form-control form-group'}))
    content = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class': 'form-control form-group'}))

    class Meta:
        model = Post
        fields = ['title', 'content']