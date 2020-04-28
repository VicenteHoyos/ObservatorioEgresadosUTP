from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
from datetime import datetime
# Create your models here.

TYPE_USERS = [
    ('egresado', 'egresado'),
    ('admin', 'admin'),
    ('superadmin', 'superadmin')
]

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class User(AbstractUser):
    is_superusuario = models.BooleanField(default=False)
    is_administrador = models.BooleanField(default=False)
    is_egresado =models.BooleanField(default=False)

    UNDEFINED = 'indef'
    MALE = 'masc'
    FEMALE = 'fem'
    GENDER_CHOICE = [
        (UNDEFINED, 'Indefinido'),
        (MALE, 'Masculino'),
        (FEMALE, 'Femenino')
    ]

    # # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # type_user = models.CharField(
    #     max_length=100,
    #     verbose_name='Tipo de usuario',
    #     choices=TYPE_USERS,
    #     default=TYPE_USERS[0][0]
    # )
    
    imagen_Perfil = models.ImageField(upload_to=upload_location,
        null = True,
        blank = True,
        )
    
    website = models.URLField(max_length=200, blank=True)
    telefono = models.IntegerField(default=0)
    # interests = models.ManyToManyField(Subject, related_name='interested_students')
    ciudad = models.CharField(max_length=30)
    dni_administrador = models.CharField(max_length=20)
    fecha_Nacimiento = models.DateField(default=datetime.now)
    genero = models.CharField(max_length=6, choices=GENDER_CHOICE, default=UNDEFINED)
    Confirmacion_manejo_datos_sensibles = models.BooleanField(default=True)
    biografia = models.TextField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True , auto_now = False)
    actualizado= models.DateTimeField(auto_now_add=False , auto_now = True)
    # created = models.DateTimeField(auto_now_add=True)
    # modified = models.DateTimeField(auto_now=True)

    #interests = models.ManyToManyField(Subject, related_name='interested_students')

    # Obtenemos los perfiles de cada usuario acorde a su tipo

    def get_superusuario_profile(self):
        superusuario_profile = None
        if hasattr(self, 'superusuarioprofile'):
            superusuario_profile=self.superusuarioprofile
        return superusuario_profile

    def get_egresado_profile(self):
        egresado_profile = None
        if hasattr(self, 'egresadoprofile'):
            egresado_profile = self.egresadoprofile
        return egresado_profile

    def get_administrador_profile(self):
        administrador_profile = None
        if hasattr(self, 'administradorprofile'):
            administrador_profile = self.administradorprofile
        return administrador_profile

    class Meta:
        db_table = 'auth_user'

    def get_absolute_url(self):
        return reverse('users:userdetail') #namespace posts
        #"/posts/%s/" %(self.id)

    def __str__(self):
        """Return username."""
        return self.username

# def create_slug(instance, new_slug= None):
#     slug = slugify(instance.user)
#     if new_slug is not None:
#         slug = new_slug
#     queryset = Profile.objects.filter(slug= slug).order_by("-id")
#     exists = queryset.exists()
#     if exists:
#         new_slug="%s-%s" %(slug, queryset.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug

# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)

# pre_save.connect(pre_save_post_receiver, sender=Profile)