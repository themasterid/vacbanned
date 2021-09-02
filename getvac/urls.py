from django.urls import path

from . import views

app_name = 'getvac'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<post_id>/edit/', views.post_edit, name='edit'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.record_create, name='create'),
    path('ok/', views.go_ok, name='ok'),
    path('info/<int:post_id>/', views.info, name='info'),
]
