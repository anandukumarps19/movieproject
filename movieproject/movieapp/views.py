from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from . models import movie

# Create your views here.
def index(request):
    user=movie.objects.all()
    return render(request,'index.html',{'movie_list':user})

def get_details(request,movie_id):
    user=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'Movie':user})

def add_movie(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        des = request.POST.get('des')
        year=request.POST.get('year')
        date = request.POST.get('date')
        image = request.FILES['image']
        film=movie(name=name,desc= des,year=year,date=date, image=image)
        film.save();
        return redirect('/')

    return render(request,'add.html')

def update(request,id):
    film=movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES, instance= film)
    if form.is_valid():
        form.save()

    return render(request,'edit.html',{'movie':film,'form':form})

def delete(request,id):
    if request.method == 'POST':
        film=movie.objects.get(id=id)
        film.delete()
        return redirect('/')
    return render(request,'delete.html')