import email
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import User
#from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    users = User.objects.all()
    page = request.GET.get('page', 1)
    
    paginator = Paginator(users, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'index.html', { 'users': users })

# Create Post
def add(request):
    template = loader.get_template('create.html')
    return HttpResponse(template.render({}, request))

# Store Blog
def addrecord(request):
    x = request.POST['first_name']
    y = request.POST['last_name']
    t = request.POST['email']
    v = request.POST['contact']
    r = request.POST['image']
    post = User(first_name=x, last_name=y, email=t, contact=v, image=r)
    post.save()
    return HttpResponseRedirect(reverse('index'))

# Delete Post
def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('index'))

# Update Post
def update(request, id):
    user = User.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'user': user,
    }
    return HttpResponse(template.render(context, request))

# Update Post
def updaterecord(request, id):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    contact = request.POST['contact']
    image = request.POST['image']
    user = User.objects.get(id=id)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.contact = contact
    user.image = image
    user.save()
    return HttpResponseRedirect(reverse('index'))

# Show Post
def show(request, id):
    user = User.objects.get(id=id)
    template = loader.get_template('show.html')
    context = {
        'user': user,
    }
    return HttpResponse(template.render(context, request))
