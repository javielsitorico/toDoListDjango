from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Tareas

def tareas(request):
    tareas = Tareas.objects.values()
    template = loader.get_template('tareas.html')
    contexto = {
        'tareas': tareas, 
    }
    return HttpResponse(template.render(contexto, request))

def realizada(request, identificador):
    tarea = Tareas.objects.get(id=identificador)
    tarea.realizada = True
    tarea.save()
    return HttpResponseRedirect(reverse('tareas'))

def nuevaTarea(request):
    desc = request.GET['descripcion']
    tarea = Tareas(descripcion = desc, realizada = False)
    tarea.save()
    return HttpResponseRedirect(reverse('tareas'))

def borrarTarea(request, identificador):
    tarea = Tareas.objects.get(id=identificador)
    tarea.delete()
    return HttpResponseRedirect(reverse('tareas'))