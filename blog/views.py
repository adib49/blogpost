from django.shortcuts import render,redirect
from .models import *

def blogs_view(request):

    if request.method =='POST':
        data = request.POST

        blog_name = data.get('blog_name')
        blog_content = data.get('blog_content')
        blog_thumbnail = request.FILES.get('blog_thumbnail')

        blogs.objects.create(
            blog_name = blog_name,
            blog_content = blog_content,
            blog_thumbnail = blog_thumbnail,
         )


        return redirect('/blog')
    return render(request,'form.html')