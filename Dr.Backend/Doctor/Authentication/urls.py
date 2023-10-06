from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('register/',RegisterUser.as_view()),
    path('me/', RetrieveUserView.as_view()),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('edit/<id>', EditUser.as_view()),
    path('user/<id>', GetUser.as_view()),
    path('admin/login', AdminLoginView.as_view()),
    path('update/user/<id>', ProfileUpdateView.as_view()),
    path('delete/<id>', DeleteUser.as_view()),
    path('admin/search/',UserSearchView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)