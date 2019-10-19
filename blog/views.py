from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Blog home</h1>')
#
# def about(request):
#     return HttpResponse('<h1>About page</h1>')

# instead of using the dummy data we will query the post model
# posts=[
#     {
#         'author':'Nishikant Tayade',
#         'title':'How are you!'
#     },
#     {
#         'author': 'Akhilesh Tayade',
#         'title': 'How are you really!'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})
