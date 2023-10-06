
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from UserAuthentication.serializer import CustomTokenObtainPairSerializer



urlpatterns = [
    path('admin/', admin.site.urls),
    path('UserAuthentication/token/', TokenObtainPairView.as_view(serializer_class=CustomTokenObtainPairSerializer), name='token_obtain_pair'),
    path('UserAuthentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('UserAuthentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('UserAuthentication-auth/', include('rest_framework.urls')),
    path('UserAuthentication/users/',include('UserAuthentication.urls')),
    path('api/feeds/', include('feeds.urls'))

]
