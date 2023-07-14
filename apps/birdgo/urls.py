from django.urls import path
from . import views

urlpatterns = [
   path('',views.home, name='index'),
   path('about',views.about),
   path('contact',views.contact),
   path('agregarAve/',views.bird_create),
   path('birds/',views.birds_list, name='birds'),
   path('birds/detail/<str:bird_id>',views.bird_detail, name='bird-detail'),
   path('birds/<str:bird_id>/delete',views.bird_delete, name='bird-delete'),
   path('birds/edit/<str:bird_id>', views.bird_update, name='bird-edit'),
]  