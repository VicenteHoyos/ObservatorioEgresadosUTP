from django import forms

from .models import Profile

class userForm(forms.ModelForm):
    class Meta:
        model = Profile
        
        fields ={"imagen_Perfil",
        "website",
        "telefono",
        "ciudad",
        "dni_administrador",
        "fecha_Nacimiento", 
        "genero",
        "confirmation_handling_sensitive_data", 
        "biografia"
        }