from django.shortcuts import HttpResponse, render
from AppCoder.models import Curso

# Create your views here.
def guardar_curso(request, nombre, camada):
    curso = Curso(nombre=nombre,camada=camada,apellido="Coderhouse")
    curso.save()
    context = {
        "nombre": nombre
    }
    return render(request, "AppCoder/guardar_curso.html", context=context)

def inicio(request):
    return render(request, "base.html")

def cursos(request):
    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos
    }
    return render(request, "AppCoder/cursos.html", context=context)

def profesores(request):
    return HttpResponse("Vista Profesores")

def estudiantes(request):
    return HttpResponse("Vista Estudiantes")

def entregables(request):
    return HttpResponse("Vista Entregables")