from django import forms

from .models import User

class userForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields ={"imagen_Perfil",
        "username",
        "first_name",
        "last_name",
        "email",
        "is_superusuario" , 
         "website",
         "telefono",
         "ciudad", 
         "dni_administrador",
         "fecha_Nacimiento",
         "genero",
         "Confirmacion_manejo_datos_sensibles",
         "biografia"
        }

class userEnableForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields ={
        "username",
        "email",
        "is_staff", 
        "is_administrador", 
        }

class userDisableForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields ={
        "username",
        "email",
        "is_staff", 
        "is_administrador", 
        }

class userAdminUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields ={
        "username",
        "first_name",
        "last_name",
        "email", 
         "website",
         "telefono",
         "ciudad", 
         "genero",
         "biografia"
        }