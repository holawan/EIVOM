from django.contrib import admin

from .models import Crew,CrewArticle,CrewReview
# Register your models here.


class CrewAdmin(admin.ModelAdmin):
    list_display = ('crewname', 'crew_location1', )


admin.site.register(Crew, CrewAdmin)

class CrewArticleAdmin(admin.ModelAdmin):
    list_display = ('title', )


admin.site.register(CrewArticle, CrewArticleAdmin)

admin.site.register(CrewReview)
