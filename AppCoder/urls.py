from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio), #Esta es nuestra primera view
    path('guardarcursos/<nombre>/<camada>', views.guardar_curso),
    path('cursos', views.cursos, name="AppCoderCursos"),
    path('profesores', views.profesores, name="AppCoderProfesores"),
    path('estudiantes', views.estudiantes, name="AppCoderEstudiantes"),
    path('entregables', views.entregables, name="AppCoderEntregables"),
]