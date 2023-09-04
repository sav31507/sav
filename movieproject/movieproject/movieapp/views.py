from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import movie

# Create your views here.
def demo(request):
    a=movie.objects.all()
    return render (request, 'index.html',{'a':a})



def demo1(request,movie_id):
    c=movie. objects.get(id=movie_id)
    return render(request, 'sav.html',{'c':c})



# in urls given the name update
def UPDATE(request, id):
    movie1=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES, instance=movie1)
    if form.is_valid():
        form.save()
        return redirect('/')
    form=MovieForm(instance=movie1)

    return render(request,'edit.html',{'form': form})



def DELETE(request, id):
    if request.method == 'POST':
        movie2=movie.objects.get(id=id)
        movie2.delete()
        return redirect('/')

    return render(request, 'delete.html')

def ADD(request):
    form=MovieForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/')
    form = MovieForm()

    return render(request , 'add.html', {'form':form})