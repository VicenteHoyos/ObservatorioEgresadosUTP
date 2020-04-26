from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q

from .forms import RegModelForm , ContactForm, InvitacionAdminForm
from .models import Registrado, Contacto, InvitacionAdmin

# Create your views here.
def inicio(request):
	titulo = "Registrate"
	# if request.user.is_authenticated:
	# 	titulo = "Bienvenid@ %s" %(request.user) #saludo 
	form = RegModelForm(request.POST or None)

	context = {
				"titulo": titulo,
				"form_comentario": form,
			}

	if form.is_valid():
		instance = form.save(commit=False)
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		# comentario = form.cleaned_data.get("comentario")
		instance = form.save(commit = False)
		form_email = form.cleaned_data.get("email")
		form_nombre = form.cleaned_data.get("nombre")
		asunto = 'Solicitud Registro Observatorio Egresados'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from]
		email_mensaje = "%s: Solicitud Registro Cuenta Enviado por %s Enviado a %s" %(form_nombre , form_email, email_to)
		send_mail(asunto, 
			email_mensaje,
			email_from,
			email_to,
			fail_silently=False
			)
		instance.user = request.user
		instance.save()	
		return HttpResponseRedirect(instance.get_absolute_url())

		if not instance.nombre:
			instance.nombre = "Anonimo"
		instance.save()

		context = {
			"titulo": "Gracias %s!" %(nombre)
		}

		if not nombre:
			context = {
				"titulo": "Gracias %s!" %(email)
			}

		#print instance
		#print instance.timestamp
		# form_data = form.cleaned_data
		# abc = form_data.get("email")
		# abc2 = form_data.get("nombre")
		# obj = Registrado.objects.create(email=abc, nombre=abc2)

	# if request.user.is_authenticated and request.user.is_staff:
	# 	context = {
	# 		"queryset":["abc","123"],
	# 	}
	return render(request, "inicio.html", context)

def invitacionAdmin(request):
	titulo = "Invitar Administrador"
	form = InvitacionAdminForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit = False)
		form_email = form.cleaned_data.get("email")
		form_nombre = form.cleaned_data.get("nombre")
		asunto = 'Invitacion Administrador Observatorio Egresados'
		link ='http://127.0.0.1:8000/accounts/register/'
		email_from = settings.EMAIL_HOST_USER
		email_to = [form_email]
		email_mensaje = "Cordial saludo %s: El presente correo es para invitarlo a formar parte del grupo de administradores de Observatorio de Egresados. Para crear su cuenta ingreser al link %s de lo contrario haga caso omiso a este correo. Enviado por %s.  " %(form_nombre,link,email_from)
		send_mail(asunto, 
			email_mensaje,
			email_from,
			email_to,
			fail_silently=False
			)
		instance.user = request.user
		instance.save()	
		messages.success(request, "Tu mensaje ha sido enviado con Exito")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form_contacto": form,
		"titulo": titulo,
	}
	return render(request, "inviteadmin.html", context)


def contacto(request):
	titulo = "Contacto"
	form = ContactForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit = False)
		form_email = form.cleaned_data.get("email")
		form_mensaje = form.cleaned_data.get("mensaje")
		form_nombre = form.cleaned_data.get("nombre")
		asunto = 'Contacto Observatorio Egresados'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, "vicente.hoyos@gmail.com"]
		email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
		send_mail(asunto, 
			email_mensaje,
			email_from,
			email_to,
			fail_silently=False
			)
		instance.user = request.user
		instance.save()	
		messages.success(request, "Tu mensaje ha sido enviado con Exito")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form_contacto": form,
		"titulo": titulo,
	}
	return render(request, "contacto.html", context)

def about(request):
	return render(request,"about.html", {})
    






