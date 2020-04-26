from django.contrib import admin

from .models import Profile
# Register your models here.

class userModelAdmin(admin.ModelAdmin):
    list_display=["type_user","imagen_Perfil", "website","telefono","ciudad", "dni_administrador","fecha_Nacimiento", "genero","confirmation_handling_sensitive_data", "biografia"]
    list_display_links=["dni_administrador"]
    list_filter = ["timestamp"]
    search_fields = ["dni_administrador"]
    # list_editable = ["titulo"] 
    class Meta:
        model = Profile


admin.site.register(Profile, userModelAdmin)
