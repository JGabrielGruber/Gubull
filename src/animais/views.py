from django.shortcuts   import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib     import messages


from .forms             import BovinoForm, FilhosForm
from .models            import Bovino, Filhos

import logging, logging.config
import sys


def bovino_list(request):
	queryset_list	= Bovino.objects.all()
	query_tipo		= request.GET.get("query_tipo")
	query_genero		= request.GET.get("query_genero")
	query_estado		= request.GET.get("query_estado")
	query_search	= request.GET.get("query_search")
	if query_tipo:
		queryset_list	= queryset_list.filter(tipo=query_tipo)
	if query_genero:
		queryset_list	= queryset_list.filter(genero=query_genero)
	if query_estado:
		queryset_list	= queryset_list.filter(estado=query_estado)
	if query_search:
		queryset_list	= queryset_list.filter(identificacao__icontains=query_search)
	context = {
		"title": "Lista de Bovinos",
		"object_list": queryset_list,
	}
	return render(request, 'bovino_list.html', context)

def bovino_create(request):
	form		= BovinoForm(request.POST or None, request.FILES or None)
	form_filho	= FilhosForm(request.POST or None)
	if form.is_valid():
		instance	= form.save(commit=False)
		filho		= form_filho.save(commit=False)
		if form_filho.cleaned_data['filhos'].all:
			filho.save()
			form_filho.save_m2m()
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
		"form_filho": form_filho
	}
	return render(request, 'bovino_form.html', context)

def bovino_detail(request, identificacao=None):
	instance	= get_object_or_404(Bovino, identificacao=identificacao)
	query_set	= Bovino.objects.all()
	if instance.filho:
		filhos	= get_object_or_404(Filhos, id=instance.filho.id)
		context		= {
			"title": instance.identificacao,
			"object": instance,
			"object_list": query_set,
			"filhos": filhos
		}
	else:
		context		= {
			"title": instance.identificacao,
			"object": instance,
			"object_list": query_set,
		}
	return render(request, 'bovino_detail.html', context)

def bovino_update(request, identificacao=None):
	instance	= get_object_or_404(Bovino, identificacao=identificacao)
	form		= BovinoForm(request.POST or None, request.FILES or None, instance=instance)
	form_filho	= FilhosForm(request.POST or None)
	if instance.filho:
		filhos	= get_object_or_404(Filhos, id=instance.filho.id)
		form_filho	= FilhosForm(request.POST or None, instance=filhos)
	if form.is_valid():
		instance	= form.save(commit=False)
		filho		= form_filho.save(commit=False)
		if form_filho.cleaned_data['filhos'].all:
			filho.save()
			form_filho.save_m2m()
			instance.filho = filho
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	if instance.filho:
		filhos	= get_object_or_404(Filhos, id=instance.filho.id)
		context		= {
			"title"	: instance.identificacao,
			"object": instance,
			"filhos": filhos,
			"form"	: form,
			"form_filho": form_filho
		}
	else:
		context		= {
			"title"	: instance.identificacao,
			"object": instance,
			"form"	: form,
			"form_filho": form_filho
		}
	return render(request, 'bovino_form.html', context)

	instance    = get_object_or_404(Bovino, identificacao=identificacao)
	form        = BovinoForm(request.POST or None, request.FILES or None, instance=instance)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Atualizado com Sucesso!!")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Erro ao Atualizar...")
	context     = {
		"title" : instance.identificacao,
		"object": instance,
		"form"  : form
	}
	return render(request, 'bovino_form.html', context)

def bovino_delete(request, identificacao=None):
	instance	= get_object_or_404(Bovino, identificacao=identificacao)
	instance.delete()
	return HttpResponseRedirect("/animais/bovinos")
