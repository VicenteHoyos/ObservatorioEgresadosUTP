from django.urls import include, path

from users import views

urlpatterns = [
    path('list_user',views.user_list, name='userlist'),     
    path('detail_user',views.user_detail, name='userdetail'),     
    path('update_user',views.user_update, name='userupdate'),     
    path('enable_admin_user',views.user_enable_admin, name='userenableadmin'),     
    path('<int:id>',views.user_enable_admin_detail, name='userenableadmindetail'),     
    path('update_admin_user_list',views.user_list_update_admin, name='userlistupdateadmin'),     
    path('update_admin_user/<int:id>',views.user_update_admin, name='userupdateadmin'), 
    path('user_list_disable_admin',views.user_list_disable_admin, name='userlistdisableadmin'),     
    path('disable_user_admin/<int:id>',views.user_disable_admin, name='userdisableadmin'),    
    path('enable_egresado_user',views.user_enable_egresado, name='userenableegresado'),
]