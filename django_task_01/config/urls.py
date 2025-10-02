from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, Http404
from django.shortcuts import render


# Fake DB for movies
movie_list = [
    {'title': '파묘', 'director': '장재현'},
    {'title': '웡카', 'director': '폴 킹'},
    {'title': '듄: 파트 2', 'director': '드니 빌뇌브'},
    {'title': '시민덕희', 'director': '박영주'},
]


def index(request):
    return HttpResponse('<h1>hello</h1>')


def book_list_view(request):
    return render(request, 'book_list.html', {'range': range(0, 10)})


def book_detail_view(request, num: int):
    return render(request, 'book_detail.html', {'num': num})


def language(request, lang: str):
    return HttpResponse(f'<h1>{lang} 언어 페이지입니다.</h1>')


def movies(request):
    return render(request, 'movies.html', {'movie_list': movie_list})


def movie_detail(request, index: int):
    if index < 0 or index >= len(movie_list):
        raise Http404
    movie = movie_list[index]
    return render(request, 'movie.html', {'movie': movie})


def gugu(request, num: int):
    context = {
        'num': num,
        'results': [num * i for i in range(1, 10)],
    }
    return render(request, 'gugu.html', context)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('book_list/', book_list_view, name='book-list'),
    path('book_list/<int:num>/', book_detail_view, name='book-detail'),
    path('language/<str:lang>/', language, name='language'),
    path('movie/', movies, name='movies'),
    path('movie/<int:index>/', movie_detail, name='movie-detail'),
    path('gugu/<int:num>/', gugu, name='gugu'),
]

