from django.db import models
from django.urls import reverse
from django.contrib import admin
from dateutil.relativedelta import relativedelta
from datetime import date, datetime
import os

class Bovino(models.Model):
	identificacao	= models.CharField("Brinco", unique=True, max_length=255)
	tipo			= models.CharField("Tipo", choices=(
			('Cria', 'Bovino de Cria'),
			('Engorda', 'Bovino de Engorda')
		), max_length=10, default='Cria')
	lote			= models.CharField("Lote", default="1", max_length=50)
	peso			= models.TextField("Peso em Kg e sua Data", blank=True, null=True)
	medicamento		= models.TextField("Medicamento e sua Data de aplicação", blank=True, null=True)
	observacao		= models.TextField("Observações e sua Data", blank=True, null=True)
	estado			= models.CharField("Estado", choices=(
			('Possui', 'Possui'),
			('Vendido', 'Vendido'),
			('Morto', 'Morto')
		), max_length=10, default='Possui')
	# insciminação

	nascimento		= models.DateField("Data de Nascimento", help_text="<p class='comment'>Escreva no seguinte formato: <em>DD/MM/AAAA</em></p>")
	genero			= models.CharField("Gênero", max_length=1, choices=(
			('M', 'Masculino'),
			('F', 'Feminino'),
		), default='M')
	filho			= models.ForeignKey("Filhos", on_delete=models.CASCADE, blank=True, null=True)

	def file_path(instance, filename):
		path	= instance.identificacao
		format	= instance.identificacao + '-' + str(datetime.today()) + '.jpg'
		return os.path.join(path, format)

	foto_um			= models.FileField("Foto Principal", upload_to=file_path, blank=True, null=True)
	foto_dois		= models.FileField("Segunda Foto", upload_to=file_path, blank=True, null=True)
	foto_tres		= models.FileField("Terceira Foto", upload_to=file_path, blank=True, null=True)
	foto_quatro		= models.FileField("Quarta Foto", upload_to=file_path, blank=True, null=True)
	updated			= models.DateTimeField("Atualizado", auto_now=True, auto_now_add=False)
	timestamp		= models.DateTimeField("Criado", auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.identificacao

	def __str__(self):
		return self.identificacao

	def get_absolute_url(self):
		return reverse('animais:detail', kwargs={'identificacao': self.identificacao})

	def get_age(self):
		today = date.today()
		delta = relativedelta(today, self.nascimento)
		return str(delta.years)

class Filhos(models.Model):
	timestamp	= models.DateTimeField(auto_now=False, auto_now_add=True)
	filhos		= models.ManyToManyField("Bovino", null=True, blank=True,
					help_text="<p class='comment'>Use CTRL para selecionar mais de um, ou deixar de selecionar um.</p>")

	def __unicode__(self):
		return str(self.id)

	def __str__(self):
		return str(self.id)
