from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    #title = forms.CharField(max_length=100)
    #content = forms.CharField(widget=forms.Textarea)
    #email = forms.EmailField(label="E-Mail")

    class Meta:
        model = Post
        fields = ['title','content', 'author']
