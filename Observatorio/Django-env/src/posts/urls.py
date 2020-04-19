from django.urls import include, path

from posts import views

urlpatterns = [
    path('',views.post_list, name='list'),
    path('create/',views.post_create),
    path('<slug:slug>/',views.post_detail, name='detail'),
    path('<slug:slug>/edit/',views.post_update, name="update"),
    path('<slug:slug>/delete/',views.post_delete),

]