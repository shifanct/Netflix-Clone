from django.shortcuts import render,HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required

@login_required
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_app/movie_list.html', {'movies': movies})



@login_required
def add_movie(request):
    if not request.user.is_superuser:
        return redirect('movie_list')
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('movie_list')
    return render(request, 'movie_app/add_movie.html', {'form': form})


# # movie_app/views.py

# from django.http import HttpResponse

# def movie_list(request):
#     return HttpResponse("🎬 Movie list page")

# def add_movie(request):
#     return HttpResponse("➕ Add movie page")

