from django.contrib import admin

from .models import Actor, Genre,Movie,Review
# Register your models here.
admin.site.register(Genre)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'tagline', 'view_count')


admin.site.register(Movie, MovieAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'content')


admin.site.register(Review, ReviewAdmin)

admin.site.register(Actor)
