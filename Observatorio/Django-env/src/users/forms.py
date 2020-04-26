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
        "is_active", 
        "is_superusuario" , 
        "is_administrador" , 
        "is_egresado",
         "website",
         "telefono",
         "ciudad", 
         "dni_administrador",
         "fecha_Nacimiento",
         "genero",
         "confirmation_handling_sensitive_data",
         "biografia"
        }