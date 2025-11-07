from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import login_page, jobs_page, protected_api

urlpatterns = [

    path('', login_page, name='login'),       
    path('jobs/', jobs_page, name='jobs'),   

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('api/protected/', protected_api, name='protected_api'),                  
]
