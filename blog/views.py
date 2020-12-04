from django.shortcuts import render
from .forms import CommentForm


# Create your views here.
from .models import Post, Comment


def blog_index(request):
    posts = Post.objects.order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog/blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "posts": posts,
        "category": category,
    }
    return render(request, "blog/blog_category.html", context)


def blog_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post, "comments": comments, "form": form,
    }
    return render(request, "blog/blog_detail.html", context)
