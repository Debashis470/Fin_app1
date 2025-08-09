from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.home, name='api_home'),
    path('register/', views.register_user, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT login
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),       # JWT refresh
     path('secure/', views.secure_data, name='secure_data'),  # 🔐 JWT protected
    
]
