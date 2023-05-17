from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/login/', views.keycloak_login, name='login'),
    path('custom_oidc_logout/', views.custom_oidc_logout, name='custom_oidc_logout'),
    path('account/create_user/', views.create_user, name='create_user'),
    path('account/forgot_password/', views.forgot_password, name='forgot_password'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('account/change_password/', views.forgot_password, name='change_password'),
    path('callback/', views.keycloak_callback, name='callback')
]
