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

from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.

from .forms import userForm
from .models import User #importo mi modelo

def user_detail(request):
    #instance= Post.objects.get(id=None)
    instance = get_object_or_404(User, id=request.user.id)
  
    context = {        
        "instance": instance,
    }

    return render(request,"user_detail.html", context)

def user_update(request):

    if not request.user.is_authenticated :
        raise Http404
    #instance= Post.objects.get(id=None)
    instance = get_object_or_404(User, id=request.user.id)

    form = userForm(request.POST or None, request.FILES or None, instance= instance)# edit el form
    
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request, "tu <a href='#'> post </a> ha sido modificado", extra_tags="html_safe")                
        return HttpResponseRedirect(instance.get_absolute_url())
    
    context = {        
        "title": "Modificar Datos Cuenta",
        "instance": instance,
        "form": form,
    }

    return render(request,"user_update.html", context)


def user_list(request):
	if request.user.is_superuser:
		queryset = User.objects.all()
	query = request.GET.get("q")
	if query:
		queryset=queryset.filter(
			Q(email__icontains=query)|
			Q(username__icontains=query)|
			Q(first_name__icontains=query)
			).distinct()

	paginator = Paginator(queryset, 1) # Show 25 contacts per page.
	page_number = request.GET.get('page')
	objects_list = paginator.get_page(page_number)
	
	context = {
		"objects_list": objects_list,
		"title": "Listado Usuarios", 
	}
	return render(request,"user_list.html", context)
