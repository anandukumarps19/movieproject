from django.shortcuts import render, redirect

# Create your views here.
from .forms import actform
from .models import Actor


def actor(request):
    star=Actor.objects.all()
    return render(request,'actors.html',{'film':star})

def identify(request,id):
    stars=Actor.objects.get(id=id)
    return render(request,'identify.html',{'film1':stars})

def addition(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        des=request.POST.get('des')
        image=request.FILES['image']
        hero=Actor(name=name,des=des,image=image)
        hero.save();
        return redirect('/')
    return render(request,'addition.html')

def update(request,id):
    hero=Actor.objects.get(id=id)
    form=actform(request.POST or None, request.FILES, instance= hero)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'star':hero,'paper':form})

def delete(request,id):
    if request.method == 'POST':
        hero=Actor.objects.get(id=id)
        hero.delete()
        return redirect('/')
    return render(request,'delete.html')