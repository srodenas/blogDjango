from django import forms 
from .models import Contacto

#Este fichero python, contendrá una clase ContactoFormulario

#https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/
class ContactoFormulario(forms.ModelForm):
    
    #Le decimos el modelo Contacto
    #Mostramos todos los campos, excepto el estado
    class Meta:
        model = Contacto
        fields = '__all__'
        exclude = ('estado',)
        
        widgets = {
            'nombre' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Escriba  el nombre',
                }
            ),
            
            'apellidos' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Escriba sus apellidos',
                    
                }
            ),
            
            
            'correo' : forms.EmailInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Escriba su correo electrónico',
                }
                
            ),
            
            'asunto' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Escriba el asunto',
                }  
            ),
            
            'mensaje' : forms.Textarea(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Escriba el cuerpo',
                }
            ),
            
        }