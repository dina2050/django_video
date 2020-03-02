from django.shortcuts import render
from .models import Movie, MovieRent
from customer.models import Customer
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import datetime

# Create your views here.
 
class MovieListView(ListView):
    model=Movie


class MovieDetailView(DetailView):
    model=Movie
   
    
class MovieCreateView(PermissionRequiredMixin,CreateView):
    model=Movie
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("movie_list")
    permission_required = ('movie.add_movie')

class MovieUpdateView(PermissionRequiredMixin,UpdateView):
    model=Movie
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("movie_list")

    permission_required = ('movie.change_movie')
class MovieDeleteView(PermissionRequiredMixin,DeleteView):
    model=Movie
    def get_success_url(self):
        return reverse_lazy("movie_list")

    permission_required = ('movie.delete_movie')


class MovieRentView(DetailView):
    model = Movie
    def get(self, request, *args, **kwargs):
        film=self.get_object()
        customer=request.user.customer
        MovieRent.objects.create(
            movie = film,
            customer = customer
        )
        return HttpResponseRedirect(reverse_lazy("movie_list"))



class MovieRentListView(ListView):
    model = MovieRent
    
class MovieReturnView(DetailView):
    model = MovieRent
    def get(self, request, *args, **kwargs):

        MovieRent.objects.filter(id=self.get_object().id).update(
            date_retur=datetime.datetime.now()
        )
        return HttpResponseRedirect(reverse_lazy("movierent_list"))
