from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import login_page, jobs_page, protected_api

urlpatterns = [
    # UI pages
    path('', login_page, name='login'),       # Login page
    path('jobs/', jobs_page, name='jobs'),    # Jobs table page

    # JWT endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Get JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Refresh token
    path('api/protected/', protected_api, name='protected_api'),                  # JWT-protected endpoint
]
