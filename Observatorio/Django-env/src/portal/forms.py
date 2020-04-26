from django import forms

from .models import Registrado,Contacto #se importa el modelo

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre", "email",]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, proveeder = email.split("@")
		dominio, extension = proveeder.split(".")
		if not dominio =="gmail":
			if not extension == "com":
				raise forms.ValidationError("Por favor utiliza un correo @gmail.com")
		return email

	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre")
		#validaciones
		return nombre

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contacto
		fields = ["nombre", "email", "comentario",]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, proveeder = email.split("@")
		dominio, extension = proveeder.split(".")
		if not dominio =="gmail":
			if not extension == "com":
				raise forms.ValidationError("Por favor utiliza un correo @gmail.com")
		return email

	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre")
		#validaciones
		return nombre