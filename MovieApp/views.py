from django.shortcuts import render
from MovieApp.forms import MovieForm
from MovieApp.models import Movies

def index_view(request):
    return render(request,'MovieApp/index.html')
def add_movie_view(request):
    FormObj = MovieForm()
    if request.method == 'POST':
        FormObj = MovieForm(request.POST)
        if FormObj.is_valid():
            print(FormObj.cleaned_data['release_date'])
            print(FormObj.cleaned_data['movie'])
            print(FormObj.cleaned_data['actor'])
            print(FormObj.cleaned_data['actress'])
            print(FormObj.cleaned_data['rating'])
            FormObj.save()
            return index_view(request)
    return render(request,'MovieApp/addmovie.html', {'form1':FormObj})

def list_movie_view(request):
    Movie_list = Movies.objects.all().order_by('-rating')
    return render(request,'MovieApp/listmovie.html',{'form1': Movie_list})
