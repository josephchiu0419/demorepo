from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from .forms import PostForm
#from django.http import HttpResponse

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    #return HttpResponse("<h1> This is About page</h1>")
    return render(request, 'blog/about.html', {'title':'About'})

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Post created for {title}!')
            return redirect('blog-home')
    else:
        form = PostForm()
    return render(request, 'blog/post.html',{'form':form})
