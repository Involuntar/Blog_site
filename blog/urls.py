from django.urls import path
from django.conf.urls.static import static
from Blog_site import settings

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('post/<int:post_id>/comment/', views.comment, name='comment')
]
urlpatterns = urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)