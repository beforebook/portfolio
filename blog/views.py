from django.shortcuts import *
from .models import Blog

# Create your views here.
def blog_page(request):
    blog = Blog.objects
    return render(request, 'blog.html', {'blog':blog})

def blog_text(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'blog_text.html', {'blog':blog})

