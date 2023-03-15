from django.shortcuts import HttpResponse, render, redirect
from AppCoder.models import Curso
from AppCoder.forms import CursoForm

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
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso_save = Curso(
                nombre=informacion["nombre"],
                camada=informacion["camada"]
            )
            curso_save.save()
    all_cursos = Curso.objects.all()
    context = {
        "cursos": all_cursos,
        "form": CursoForm()
    }
    return render(request, "AppCoder/cursos.html", context=context)

def profesores(request):
    return HttpResponse("Vista Profesores")

def estudiantes(request):
    return HttpResponse("Vista Estudiantes")

def entregables(request):
    return HttpResponse("Vista Entregables")
