from django.contrib import admin

# Register your models here.
from .forms import RegModelForm, ContactForm #formulario
from .models import Registrado, Contacto

class AdminRegistrado(admin.ModelAdmin):
	list_display = ["email", "nombre","comentario", "timestamp"]
	form = RegModelForm
	# list_display_links = ["nombre"]
	list_filter = ["timestamp"]
	list_editable = ["nombre"]
	search_fields = ["email", "nombre"]
	# class Meta:
	# 	model = Registrado

class AdminContacto(admin.ModelAdmin):
	list_display = ["email", "nombre","comentario", "timestamp"]
	form = ContactForm 
    # list_display_links = ["nombre"]
	list_filter = ["timestamp"]
	list_editable = ["nombre"]
	search_fields = ["email", "nombre"]

myModels = [Registrado,Contacto]  # iterable list
admin.site.register(myModels)
#admin.site.register(Registrado, AdminRegistrado)