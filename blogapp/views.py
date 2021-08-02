from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from blogapp import forms
from blogapp import models

@login_required(login_url='/login/')
def home(request):
  blog = models.BlogModel.objects.all()
  context = {'blog':blog}
  return render(request, 'home.html',context)

def login_view(request):
  return render (request,'login.html')

def logout_view(request):
  logout(request)
  return redirect('/')

def register_view(request):
  return render (request, 'register.html')

def add_blog(request):
  context = {'form':forms.Blogform}
  try:
    if request.method == "POST":
      form = forms.Blogform(request.POST)
      image = request.FILES['image']
      title = request.POST.get('title')
      user = request.user
      
      if form.is_valid():
        content = form.cleaned_data['content']
      
      blog_obj = models.BlogModel.objects.create(
        user=user,title=title,content=content,
        image=image
      )
      print(blog_obj)
      return redirect('/add_blog/')
      
  except Exception as e:
    print(e)
  
  return render (request, 'add_blog.html',context)


def blog_detail(request,slug):
  context = {}
  try:
    blog_obj = models.BlogModel.objects.filter(slug=slug).first()
    context['blog_obj'] = blog_obj
  except Exception as e:
    print(e)
  return render(request, 'blog_detail.html',context)

def see_blog(request):
  context = {}
  try:
    blog_objs = models.BlogModel.objects.filter(user=request.user)
    context['blog_objs'] = blog_objs
  except Exception as e:
    print(e)
  return render(request,'see_blog.html', context)

def blog_delete(request,id):
  try:
    blog_obj = models.BlogModel.objects.get(id=id)
    if blog_obj.user == request.user:
      blog_obj.delete()
      
  except Exception as e:
    print(e)
  return redirect('/see_blog/')


def blog_update(request, slug):
  blog_obj = models.BlogModel.objects.get(slug=slug)
  
  form = forms.Blogform(instance=blog_obj)
  
  if request.method == "POST":
    form = forms.Blogform(request.POST)
    image = request.FILES['image']
    title = request.POST.get('title')
    if form.is_valid():
      content = form.cleaned_data['content']
    
    blog_obj.title = title
    blog_obj.image =image
    blog_obj.content = content   
    blog_obj.save()
    return redirect('/see_blog/')
  
  return render(request,'blog_update.html',{'form':form})
