from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from .models import *
from .forms import *


def home(request):
    return render(request,"index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

""" funcion para agregar """

def bird_create(request):
    if request.method == 'POST':
        form = BirdsForm(request.POST, request.FILES)
        if form.is_valid(): 
            id_ave = form.cleaned_data.get('id_ave')
            nombre_ave = form.cleaned_data.get('nombre_ave')
            nombre_cientifico = form.cleaned_data.get('nombre_ave')
            imagen_ave = form.cleaned_data.get('imagen_ave')
            print('img')
            obj = Bird.objects.create(
                id_ave = id_ave, 
                nombre_ave = nombre_ave, 
                nombre_cientifico = nombre_cientifico,
                imagen_ave = imagen_ave
            )
            print('objeto', obj)
            obj.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        form = BirdsForm
    return render(request,'formularioAves.html', {'form':form})

def birds_list(request):
    context = {'birds': Bird.objects.all()}
    return render(request,'birds-list.html',context)

def bird_detail(request, bird_id):
    try:
        bird = Bird.objects.get(id_ave=bird_id)
        if bird:
            context = {'bird':bird}
            return render(request,'bird-detail.html',context)
        else:
            return redirect(reverse('birds') + '?NO_EXISTS')
    except:
        return redirect(reverse('birds') + '?FAIL')
    
def bird_delete(request, bird_id):
    try:
        print('borrando...')
        bird = Bird.objects.get(id_ave=bird_id)
        bird.delete()
        return HttpResponseRedirect(reverse('birds') + '?DELETED')
    except:
        return redirect(reverse('birds') + '?FAIL')
    
def bird_update(request,bird_id):
    try:
        bird = Bird.objects.get(id_ave = bird_id)
        form = BirdsForm(instance=bird)

        if request.method == 'POST':
            form = BirdsForm(request.POST, request.FILES, instance=bird)
            if form.is_valid():
                form.save()
                return redirect(reverse('birds') + '?UPDATED')
            else:
                return redirect(reverse('bird-edit') + bird_id) 

        context = {'form':form}
        return render(request,'bird-edit.html',context)
    except:
        return redirect(reverse('birds') + '?NO_EXISTS')