from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def get_index(request):
    posts = Post.objects.all()
    return render(request, "blog/get_index.html", {'posts':posts})
    
def read_post(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "blog/read_post.html", {"post":post} )
    
    
    
def write_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        post = form.save()
        return redirect(read_post, post.id)
    else:    
        form = PostForm()
        return render(request, "blog/post_form.html", {'form': form })
    
 


def edit_read_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method=="POST":
        form = PostForm(request.POST, instance=post)
        form.save()
        return redirect(read_post, id)
    else:
        form=PostForm(instance=post)
        return render(request, "blog/post_form.html", {"form":form})
