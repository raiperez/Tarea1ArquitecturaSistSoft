from django.shortcuts import render, redirect
from home.models import Comment
from home.forms import CommentForm
from home.utils import get_client_ip

# Create your views here.
def home(request):
    comments = Comment.objects.all().order_by("-created_at")
    form = CommentForm()

    return render(request, 'base.html', {
        'comments': comments,
        'form': form,
        })

#### API ####

def post_comment(request):
    form = CommentForm(request.POST or None)
    data = {'form': form}

    if form.is_valid():
        ip_address = get_client_ip(request)
        form.save(ip_address)
        return redirect('home')

    return render(request, 'base.html', data)
