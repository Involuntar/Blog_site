from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post_get, name='post_get'),
    path('post/<int:post_id>/comment/', views.comment_create, name='comment_create')
]