from django.contrib import admin
from .models import Movie, MovieGenre, MovieRent
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(MovieGenre)
class MovieGenreAdmin(admin.ModelAdmin):
    pass

@admin.register(MovieRent)
class MovieRentAdmin(admin.ModelAdmin):
    list_display = ("id","movie","customer","date_out", "date_retur")
    list_editable = ("date_retur",)
    pass