from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

        widgets = {
             "copiaDNI_A":forms.ChoiceField(choices=[('si', 'Si'), ('no', 'No')], widget=forms.RadioSelect),
            'fechanacimientoA': forms.DateInput(attrs={'type': 'date'})
            
        }
