from django import forms
from django_select2.forms import Select2MultipleWidget
import json

class BovinoForm(forms.ModelForm):
	from .models import Bovino, Filhos

	identificacao	= forms.CharField(label="Brinco", max_length=255)
	nascimento		= forms.DateField(label="Data de Nascimento")
	genero			= forms.ChoiceField(label="Gênero", choices=(
			('M', 'Masculino'),
			('F', 'Feminino'),
		))
	#filho			= forms.ManyToManyField("self", null=True, blank=True,
	#					help_text="<p class='comment'>Use CTRL para selecionar mais de um, ou deixar de selecionar um.</p>")
	foto_um			= forms.FileField(label="Foto Principal", required=False)
	foto_dois		= forms.FileField(label="Segunda Foto", required=False)
	foto_tres		= forms.FileField(label="Terceira Foto", required=False)
	foto_quatro		= forms.FileField(label="Quarta Foto", required=False)
	#filho			= forms.ChoiceField(required=False, choices=Filhos.objects.all())


	class Meta:
		from .models import Bovino
		model = Bovino
		fields = [
			'identificacao',
			'tipo',
			'peso',
			'medicamento',
			'nascimento',
			'genero',
			'foto_um',
			'foto_dois',
			'foto_tres',
			'foto_quatro',
			'filho',
			'estado'
		]
		widgets = {
			'peso'			: forms.HiddenInput(),
			'medicamento'	: forms.HiddenInput(),
			'filho'			: forms.HiddenInput()
		}

class FilhosForm(forms.ModelForm):
	from .models import Bovino

	filhos	= forms.ModelMultipleChoiceField(label="Filhos", required=False, queryset=Bovino.objects.all(), widget=Select2MultipleWidget)
	#filhos			= forms.ModelMultipleChoiceField(required=False, queryset=Bovino.objects.all())

	class Meta:
		from .models import Filhos
		model	= Filhos
		fields	= [
			'filhos'
		]
