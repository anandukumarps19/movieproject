from . import views
from django.urls import path, include
app_name='movieapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.get_details,name='get_details'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('Delete/<int:id>/',views.delete, name='delete')


]