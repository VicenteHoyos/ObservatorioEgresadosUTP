from django.urls import include, path

from users import views

urlpatterns = [
    path('listuser',views.user_list, name='userlist'),     
    path('detailuser',views.user_detail, name='userdetail'),     

]