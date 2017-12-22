#-*- coding: utf-8 -*-
from django import forms

"""
Constantes
"""
ERROR_MESSAGE_NOMBRE = {'required':'El nombre es requerido'}
ERROR_MESSAGE_EMAIL = {'required':'El correo es requerido', 'invalid':'Ingrese un correo válido'}
ERROR_MESSAGE_MENSAJE = {'required':'El mensaje es requerido'}

class ContactenosForm(forms.Form):
    nombre = forms.CharField(max_length=20, error_messages=ERROR_MESSAGE_NOMBRE)
    correo = forms.CharField(error_messages=ERROR_MESSAGE_EMAIL)
    mensaje = forms.CharField(widget=forms.Textarea, error_messages=ERROR_MESSAGE_MENSAJE)

    def __init__(self, *args, **kwargs):
        super(ContactenosForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'id':'nombre', 'class':'validate'})
        self.fields['correo'].widget.attrs.update({'id':'email','class':'validate'})
        self.fields['mensaje'].widget.attrs.update({'id':'mensaje','class':'materialize-textarea'})
