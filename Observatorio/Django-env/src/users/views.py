from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from urllib.parse import quote_plus
from django.db.models import Prefetch

from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.

from .forms import userForm, userEnableForm, userAdminUpdateForm , userDisableForm
from .models import User #importo mi modelo
from portal.models import InvitacionAdmin, Registrado

def user_detail(request):
    #instance= Post.objects.get(id=None)
    instance = get_object_or_404(User, id=request.user.id)
  
    context = {        
        "instance": instance,
    }

    return render(request,"user_detail.html", context)

def user_enable_admin(request):
    listquery=[]
    if not request.user.is_authenticated :
        raise Http404

    if request.user.is_superuser:
        queryset = InvitacionAdmin.objects.all()
        querysetusers = User.objects.all()
        
    if len(querysetusers) >= len(queryset):
        for u in querysetusers:
            for u2 in queryset:
                if (u.email)==(u2.email):
                    if not u.is_staff:
                        listquery.append(u)
                else:
                    pass
    else:
        for u in queryset:
            for u2 in querysetusers:
                if (u.email)==(u2.email):
                    if not u2.is_staff:
                        listquery.append(u2)
                else:
                    pass
    paginator = Paginator(listquery, 1) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    objects_list = paginator.get_page(page_number)
    
    context = {
        "objects_list": objects_list,
        "title": "Listado Usuarios", 
    }

    return render(request,"user_enable_admin.html", context)

def user_enable_admin_detail(request, id=None):
    if not request.user.is_authenticated :
        raise Http404
    instance = get_object_or_404(User, id=id)

    form = userEnableForm(request.POST or None, request.FILES or None, instance= instance)# edit el form
    
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request, "Cuenta Administrador Habilitada", extra_tags="html_safe")                
        return HttpResponseRedirect(instance.get_absolute_url())
    
    context = {        
        "instance": instance,
        "form": form,
        }
    return render(request,"user_enable_admin_detail.html", context)

def user_list_disable_admin(request):
	if request.user.is_superuser:
		queryset = User.objects.filter(is_staff = True, is_administrador=True)
	
	query = request.GET.get("q")
	if query:
		queryset=queryset.filter(
			Q(email__icontains=query)|
			Q(username__icontains=query)|
			Q(first_name__icontains=query)|
			Q(last_name__icontains=query)
			).distinct()

	paginator = Paginator(queryset, 1) # Show # contacts per page.
	page_number = request.GET.get('page')
	objects_list = paginator.get_page(page_number)
	
	context = {
		"objects_list": objects_list,
		"title": "Listado Administradores", 
	}
	return render(request,"user_list_disable_admin.html", context)

def user_disable_admin(request, id=None):
    if not request.user.is_authenticated :
        raise Http404
    instance = get_object_or_404(User, id=id)

    form = userDisableForm(request.POST or None, request.FILES or None, instance= instance)# edit el form
    
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request, "Cuenta Administrador Habilitada", extra_tags="html_safe")                
        return HttpResponseRedirect(instance.get_absolute_url())
    
    context = {        
        "instance": instance,
        "form": form,
        }
    return render(request,"user_disable_admin.html", context)

def user_update(request):
    #modificar datos propia cuenta
    if not request.user.is_authenticated :
        raise Http404
    #instance= Post.objects.get(id=None)
    instance = get_object_or_404(User, id=request.user.id)

    form = userForm(request.POST or None, request.FILES or None, instance= instance)# edit el form
    
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request, "Tus datos han sido modificados", extra_tags="html_safe")                
        return HttpResponseRedirect(instance.get_absolute_url())
    
    context = {        
        "title": "Modificar Datos Cuenta",
        "instance": instance,
        "form": form,
    }

    return render(request,"user_update.html", context)

def user_list_update_admin(request):
	if request.user.is_superuser:
		queryset = User.objects.filter(is_staff = True, is_administrador=True)
	
	query = request.GET.get("q")
	if query:
		queryset=queryset.filter(
			Q(email__icontains=query)|
			Q(username__icontains=query)|
			Q(first_name__icontains=query)|
			Q(last_name__icontains=query)
			).distinct()

	paginator = Paginator(queryset, 1) # Show # contacts per page.
	page_number = request.GET.get('page')
	objects_list = paginator.get_page(page_number)
	
	context = {
		"objects_list": objects_list,
		"title": "Listado Administradores", 
	}
	return render(request,"user_list_update_admin.html", context)

def user_update_admin(request, id=None):
    if not request.user.is_authenticated :
        raise Http404
    #instance= Post.objects.get(id=None)
    instance = get_object_or_404(User, id=id)

    form = userAdminUpdateForm(request.POST or None, request.FILES or None, instance= instance)# edit el form
    
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request, "Tu Informacion ha sido modificado", extra_tags="html_safe")                
        return HttpResponseRedirect(instance.get_absolute_url())
    
    context = {        
        "title": "Modificar Datos Cuenta",
        "instance": instance,
        "form": form,
    }

    return render(request,"user_update_admin.html", context)

def user_list(request):
	if request.user.is_superuser:
		queryset = User.objects.filter(is_staff = True, is_administrador=True)
	
	query = request.GET.get("q")
	if query:
		queryset=queryset.filter(
			Q(email__icontains=query)|
			Q(username__icontains=query)|
			Q(first_name__icontains=query)|
			Q(last_name__icontains=query)
			).distinct()

	paginator = Paginator(queryset, 1) # Show # contacts per page.
	page_number = request.GET.get('page')
	objects_list = paginator.get_page(page_number)
	
	context = {
		"objects_list": objects_list,
		"title": "Listado Administradores", 
	}
	return render(request,"user_list.html", context)

def user_enable_egresado(request):
    listquery=[]
    if not request.user.is_authenticated :
        raise Http404

    if request.user.is_staff and request.user.is_administrador:
        queryset = Registrado.objects.all()
        querysetusers = User.objects.all()
        
    if len(querysetusers) >= len(queryset):
        for u in querysetusers:
            for u2 in queryset:
                if (u.email)==(u2.email):
                    if not u.is_staff:
                        listquery.append(u)
                else:
                    pass
    else:
        for u in queryset:
            for u2 in querysetusers:
                if (u.email)==(u2.email):
                    if not u2.is_staff:
                        listquery.append(u2)
                else:
                    pass
    paginator = Paginator(listquery, 1) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    objects_list = paginator.get_page(page_number)
    
    context = {
        "objects_list": objects_list,
        "title": "Listado Solicitudes Egresados", 
    }

    return render(request,"user_enable_egresado.html", context)