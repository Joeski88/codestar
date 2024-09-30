from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post, About
from .forms import CommentForm

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter()
    template_name = "index.html"
    paginate_by = 6

def post_detail(request, slug):

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        print("Recieved a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, message.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    comment_form = CommentForm()
    print("About to render template")

    return render(
        request, 
        "blog/post_detail.html", 
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
        )
    
def about_view(request):
    about = About.objects.all().order_by('-updated_on').first()
    return render(request, 'about/about.html', {"about": about},)