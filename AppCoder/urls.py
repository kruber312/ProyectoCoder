from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio), #Esta es nuestra primera view
    path('curso/<camada>', views.guardar_curso),
    path('cursos', views.cursos),
    path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('entregables', views.entregables),
]