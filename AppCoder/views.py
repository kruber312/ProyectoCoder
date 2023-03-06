from django.shortcuts import HttpResponse
from AppCoder.models import Curso


# Create your views here.
def guardar_curso(request, camada):
    curso = Curso(nombre="HTML",camada=camada,apellido="Coderhouse")
    curso.save()
    return HttpResponse("Usuario creado exitosamente")

def inicio(request):
    return HttpResponse("Vista Inicio")

def cursos(request):
    return HttpResponse("Vista Cursos")

def profesores(request):
    return HttpResponse("Vista Profesores")

def estudiantes(request):
    return HttpResponse("Vista Estudiantes")

def entregables(request)
    return HttpResponse("Vista Entregables")