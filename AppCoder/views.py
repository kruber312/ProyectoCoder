from django.shortcuts import HttpResponse
from AppCoder.models import Curso


# Create your views here.
def guardar_curso(request, camada):
    curso = Curso(nombre="HTML",camada=camada,apellido="Coderhouse")
    curso.save()
    return HttpResponse("Usuario creado exitosamente")