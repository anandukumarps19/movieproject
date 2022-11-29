
from django.urls import path, include
from .import views

app_name='Actors'

urlpatterns = [

    path('',views.actor,name='actor'),
    path('actor/<int:id>/',views.identify, name='identify'),
    path('addition/',views.addition, name='addition'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')


]
