from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

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
        return redirect('/blog/')

    queryset = blogs.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(blog_name__icontains = request.GET.get('search'))
    
    context = {
        'blog_list': queryset
    }
    
    return render(request,'form.html',context)

def delete_blog(request,id):
    queryset = blogs.objects.get(id = id)
    queryset.delete()
    return redirect('/blog/')

def update_blog(request,id):
    queryset = blogs.objects.get(id = id)
    
    if request.method =='POST':
        data = request.POST

        blog_name = data.get('blog_name')
        blog_content = data.get('blog_content')
        blog_thumbnail = request.FILES.get('blog_thumbnail')

        
        
        queryset.blog_name = blog_name
        queryset.blog_content = blog_content



        if blog_thumbnail:
            queryset.blog_thumbnail = blog_thumbnail

        queryset.save()
        return redirect('/blog/')

        
    context = {
        'blogy': queryset
        }

    return render(request,'update-form.html',context)
    
    
            