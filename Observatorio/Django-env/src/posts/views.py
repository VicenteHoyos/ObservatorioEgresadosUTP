from urllib.parse import quote_plus
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from django.utils import timezone
from django.db.models import Q
# Create your views here.

from .forms import PostForm
from .models import Post #importo mi modelo


def post_create(request):
    if not request.user.is_staff :
        print("Bienvenido %s" %(request.user))
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    #if request.method == "POST":
    #print (request.POST.get("titulo"))
    if form.is_valid():
        instance = form.save(commit = False)
        #print( form.cleaned_data.get("titulo"))
        instance.user = request.user
        instance.save()
        messages.success(request, "tu Noticia ha sido creado con exito")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {        
        "form": form,
    }
    return render(request,"post_form.html", context)

def post_detail(request, slug=None):
    #instance= Post.objects.get(id=None)
    instance = get_object_or_404(Post, slug=slug)
    if instance.publish > timezone.now().date() or instance.draft:
        if not request.user.is_staff:
            raise Http404    
    share_string = quote_plus(instance.titulo)
    context = {        
        "title": instance.titulo,
        "instance": instance,
        "share_string":share_string,
    }
    return render(request,"post_detail.html", context)

def post_list(request):
    hoy = timezone.now().date()
    queryset = Post.objects.active()#filter(draft=False).filter(publish__lte= timezone.now())#all(),order_by("-timestamp")
    if request.user.is_staff:
        queryset = Post.objects.all()
    query = request.GET.get("q")
    if query:
        queryset=queryset.filter(
            Q(titulo__icontains=query)|
            Q(contenido__icontains=query)|
            Q(user__first_name__icontains=query)
            ).distinct()
    paginator = Paginator(queryset, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    objects_list = paginator.get_page(page_number)
    
    context = {
        "objects_list": objects_list,
        "title": "Listado Noticias", 
        "hoy": hoy,        
    }
    return render(request,"post_list.html", context)

def post_update(request, slug= None):
    if not request.user.is_staff :
        raise Http404
    instance = get_object_or_404(Post, slug=slug) 

    form = PostForm(request.POST or None, request.FILES or None, instance= instance)# edit el form
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request, "tu <a href='#'> post </a> ha sido modificado", extra_tags="html_safe")                
        return HttpResponseRedirect(instance.get_absolute_url())    

    context = {        
        "title": instance.titulo,
        "instance": instance,
        "form": form,
    }
    return render(request,"post_form.html", context)

def post_delete(request, slug=None):
    if not request.user.is_staff:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "tu post ha sido Eliminado")
    return redirect("posts:list")