from django.urls import path
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('posts/create/', CreatePostView.as_view(), name='create-post'),
    path('posts/<id>', DoctorPostsListView.as_view(), name='doctor-posts-list'),
     path('slots/', DoctorSlotView.as_view(), name='time-slot-api'),

    path('getposts/',PostListView.as_view()),
    path('feeds/',PostViewset.as_view({
        'get':'list',
        'post':'create',
    })),
    path('feeds/<pk>/',PostViewset.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy',
    })),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)