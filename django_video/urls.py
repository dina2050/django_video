"""django_video URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from customer.views import HomePageView
from movies.views import MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView, MovieDeleteView, MovieRentView, MovieRentListView, MovieReturnView
from  django.conf.urls.i18n import i18n_patterns
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path("",HomePageView.as_view(),name="homepage"),
    path('customer/', include('userena.urls')),
    path('movies/', MovieListView.as_view(),name="movie_list" ),
    path('rented/', MovieRentListView.as_view(),name="movierent_list" ),
    path('movie/<pk>/', MovieDetailView.as_view(),name="movie_detail" ),
    path('movie/create', MovieCreateView.as_view(),name="movie_create" ),
    path('movie/<pk>/edit', MovieUpdateView.as_view(),name="movie_update" ),
    path('movie/<pk>/delete', MovieDeleteView.as_view(),name="movie_delete" ),
    path('movie/rent/<slug:pk>/', MovieRentView.as_view(), name='movie_rent'),
    path('movie/return/<int:pk>/', MovieReturnView.as_view(), name='movie_return')
    )
