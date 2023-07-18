from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Persona
from django.views.generic import ListView

# Create your views here.

def index(request):
    if request.method == 'POST':
        nombre_completo = request.POST['nombre_completo'].upper()
        peso = float(request.POST['peso'])
        talla = float(request.POST['talla'])
        
        if peso:
            peso = peso * 1000
        if talla:
            talla = talla * 100
        
        Persona.objects.create(
            nombre_completo = nombre_completo,
            peso = peso,
            talla = talla
        )
        
        return redirect('/')
    else:        
        personas = Persona.objects.all().order_by('id')
        
        for persona in personas:
            peso_kg = float(persona.peso)/1000
            persona.peso = f'{peso_kg:.2f}'
            talla_mt = float(persona.talla)/100
            persona.talla = f'{talla_mt:.2f}'
            
        return render(request, 'index.html', {'personas':personas})
    
def editar(request, id):
    persona = Persona.objects.get(id=id)
    
    peso_kg = float(persona.peso)/1000
    persona.peso = f'{peso_kg:.2f}'
    talla_mt = float(persona.talla)/100
    persona.talla = f'{talla_mt:.2f}'
    
    return render(request, 'editar.html', {'persona':persona})

def editar_persona(request):
    persona = Persona.objects.filter(id = request.POST['id'])
    peso = float(request.POST['peso'])
    talla = float(request.POST['talla'])
    
    if peso:
        peso = peso * 1000
    if talla:
        talla = talla * 100
    
    persona.update(
        peso = peso,
        talla = talla
    )
    return redirect('/')

def eliminar(request, id):
    Persona.objects.filter(id = id).delete()
    return redirect('/')