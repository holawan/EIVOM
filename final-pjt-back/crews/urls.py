from django.urls import path
from . import views
app_name='crews'

urlpatterns = [
    path('',views.crew_list,name='crew_list'),
    path('crew_create/',views.crew_create,name='crew_create'),
    path('<int:crew_pk>/',views.crew_datail_or_update_or_signup,name='crew'),
]