from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio), #Esta es nuestra primera view
    path('guardarcursos/<nombre>/<camada>', views.guardar_curso),
    path('cursos', views.cursos, name="AppCoderCursos"),
    path('cursos/eliminar/<camada>', views.eliminar_curso, name="AppCoderEliminar"),
    path('cursos/editar/<camada>', views.editar_curso, name="AppCoderEditar"),
    path('cursos/crear', views.crear_curso, name="AppCoderCrearCursos"),
    path('profesores', views.profesores, name="AppCoderProfesores"),
    path('estudiantes', views.estudiantes, name="AppCoderEstudiantes"),
    path('entregables', views.entregables, name="AppCoderEntregables"),
    path('buscar_curso', views.busqueda_curso, name="BuscarCurso"),
]