from . import views
from django.urls import path

urlpatterns = [
    path('', views.tareas, name='tareas'),
    path('realizada/<int:identificador>', views.realizada, name='realizada'),
    path('nuevaTarea/', views.nuevaTarea, name='realizada'),
    path('borrar/<int:identificador>', views.borrarTarea, name='borrar'),
]
