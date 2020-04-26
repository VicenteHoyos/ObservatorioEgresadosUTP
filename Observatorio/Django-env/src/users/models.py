from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.

TYPE_USERS = [
    ('egresado', 'egresado'),
    ('admin', 'admin'),
    ('superadmin', 'superadmin')
]

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Profile(models.Model):

    UNDEFINED = 'indef'
    MALE = 'masc'
    FEMALE = 'fem'
    GENDER_CHOICE = [
        (UNDEFINED, 'Indefinido'),
        (MALE, 'Masculino'),
        (FEMALE, 'Femenino')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_user = models.CharField(
        max_length=100,
        verbose_name='Tipo de usuario',
        choices=TYPE_USERS,
        default=TYPE_USERS[0][0]
    )
    
    imagen_Perfil = models.ImageField(upload_to=upload_location,
        null = True,
        blank = True,
        height_field="height_field", 
        width_field="width_field")
    
    website = models.URLField(max_length=200, blank=True)
    telefono = models.IntegerField(default=0)
    # interests = models.ManyToManyField(Subject, related_name='interested_students')
    ciudad = models.TextField(max_length=20)
    dni_administrador = models.CharField(max_length=20)
    fecha_Nacimiento = models.DateField(auto_now_add=False , auto_now = False)
    genero = models.CharField(max_length=6, choices=GENDER_CHOICE, default=UNDEFINED)
    confirmation_handling_sensitive_data = models.BooleanField(default=True)
    biografia = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True , auto_now = False)
    actualizado= models.DateTimeField(auto_now_add=False , auto_now = True)
    # created = models.DateTimeField(auto_now_add=True)
    # modified = models.DateTimeField(auto_now=True)

    #interests = models.ManyToManyField(Subject, related_name='interested_students')


    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def get_absolute_url(self):
        return reverse('users:detailuser', kwargs={"slug":self.slug}) #namespace posts
        #"/posts/%s/" %(self.id)

    def __str__(self):
        """Return username."""
        return self.user.username

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