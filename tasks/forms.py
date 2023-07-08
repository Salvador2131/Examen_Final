from django import forms

from .models import Artista_Model, Obra_Model


class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista_Model
        fields = ['name', 'surname', 'email', 'phone', 'bio']

    def __init__(self, *args, **kwargs):
        super(ArtistaForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['surname'].required = True
        self.fields['email'].required = True
        self.fields['name'].label = 'Nombre'
        self.fields['surname'].label = 'Apellido'
        self.fields['email'].label = 'Correo'
        self.fields['phone'].label = 'Telefono'
        self.fields['bio'].label = 'Biografia'
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['surname'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['bio'].widget.attrs.update({'class': 'form-control'})


class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra_Model
        fields = ['title', 'description', 'artista']

    def __init__(self, *args, **kwargs):
        super(ObraForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['description'].required = True
        self.fields['artista'].required = True
        self.fields['title'].label = 'Titulo'
        self.fields['description'].label = 'Descripción'
        self.fields['artista'].label = 'Artista'
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['artista'].widget.attrs.update({'class': 'form-control'})
