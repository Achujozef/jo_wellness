
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from Authentication.serializer import CustomTokenObtainPairSerializer



urlpatterns = [
    path('admin/', admin.site.urls),
    path('Authentication/token/', TokenObtainPairView.as_view(serializer_class=CustomTokenObtainPairSerializer), name='token_obtain_pair'),
    path('Authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('Authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('Authentication-auth/', include('rest_framework.urls')),
    path('Authentication/users/',include('Authentication.urls')),
    path('slot_post/users/',include('slot_post.urls')),
    path('get/post/',include('slot_post.urls'))


]
