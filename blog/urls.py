from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
     path('post/new/', views.post_new, name="post_new"),
     path('post/<int:pk>/edit/',views.post_edit,name="post_edit")
]