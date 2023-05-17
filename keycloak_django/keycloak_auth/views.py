from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .auth import KeycloakOIDCAuthenticationBackend
from .my_forms import UserProfileForm
from .utils.keycloak_common import server_url, realm_name, client_id, redirect_uri, keycloak_backend, logout_endpoint
from .keycloak import keycloak_admin
from .models import CustomUser

backend = KeycloakOIDCAuthenticationBackend()


def home(request):
    return render(request, 'home.html')


def keycloak_login(request):
    # Redirigez vers Keycloak pour se connecter
    return backend.authenticate_keycloak(request)


def keycloak_callback(request):
    user = backend.otp_callback(request)
    if user is not None:
        login(request, user, backend=keycloak_backend)
        return HttpResponseRedirect('/')  # Redirigez vers la page que vous voulez après la connexion
    else:
        # Réponse indiquant que l'authentification a échoué, ou rediriger vers une page d'erreur.
        return HttpResponseRedirect('/login-error')


def custom_oidc_logout(request):
    logout(request)
    # Set a redirection URL to trigger logout on the Keycloak side
    redirect_url = request.build_absolute_uri(reverse('home'))
    return HttpResponseRedirect(f'{logout_endpoint}?redirect_uri={redirect_url}')


def create_user(request):
    # Redirigez vers Keycloak pour s'inscrire
    register_url = f"{server_url}realms/{realm_name}/protocol/openid-connect/registrations?client_id={client_id}&response_type=code&scope=openid&redirect_uri={redirect_uri}"
    return HttpResponseRedirect(register_url)


def forgot_password(request):
    # Redirigez vers Keycloak pour réinitialiser le mot de passe
    reset_url = f"{server_url}realms/{realm_name}/login-actions/reset-credentials"
    return HttpResponseRedirect(reset_url)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # Get cleaned data
            data = form.cleaned_data

            # Get the user in Django's database
            try:
                django_user = CustomUser.objects.get(email=request.user.email)
            except User.DoesNotExist:
                messages.error(request, 'User not found in Django database.')
                return redirect('home')

            # Update user information in Django
            django_user.first_name = data.get('first_name')
            django_user.last_name = data.get('last_name')
            django_user.birth = data.get('birth')
            django_user.email = data.get('email')
            django_user.phone = data.get('phone')
            django_user.address = data.get('address')  # assuming you have these fields in form
            django_user.postal_code = data.get('postal_code')
            # ... update any other fields you have in your form and model
            django_user.save()

            # Get the Keycloak user ID by searching with email
            existing_users = keycloak_admin.get_users({'email': request.user.email})
            if not existing_users:
                messages.error(request, 'User not found in Keycloak.')
                return redirect('home')

            # Update user information in Keycloak
            user_id = existing_users[0]['id']
            keycloak_admin.update_user(user_id, {
                'firstName': data.get('first_name'),
                'lastName': data.get('last_name'),
                'email': data.get('email'),
            })

            messages.success(request, 'Your profile has been successfully updated.')
            return redirect('home')
    else:
        # Get the user in Django's database
        try:
            django_user = CustomUser.objects.get(email=request.user.email)
        except User.DoesNotExist:
            messages.error(request, 'User not found in Django database.')
            return redirect('home')

        # Load the current user information from Django database
        initial_data = {
            'first_name': django_user.first_name,
            'last_name': django_user.last_name,
            'email': django_user.email,
            'address': django_user.address,  # assuming you have these fields in form
            'phone': django_user.phone,  # assuming you have these fields in form
            # ... add any other fields you have in your form and model
        }
        form = UserProfileForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'profile.html', context)


def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # Get cleaned data
            data = form.cleaned_data

            # Get the user in Django's database
            try:
                django_user = CustomUser.objects.get(email=request.user.email)
            except User.DoesNotExist:
                messages.error(request, 'User not found in Django database.')
                return redirect('home')

            # Update user information in Django
            django_user.first_name = data.get('first_name')
            django_user.last_name = data.get('last_name')
            django_user.birth = data.get('birth')
            django_user.email = data.get('email')
            django_user.phone = data.get('phone')
            django_user.address = data.get('address')  # assuming you have these fields in form
            django_user.postal_code = data.get('postal_code')
            # ... update any other fields you have in your form and model
            django_user.save()

            # Get the Keycloak user ID by searching with email
            existing_users = keycloak_admin.get_users({'email': request.user.email})
            if not existing_users:
                messages.error(request, 'User not found in Keycloak.')
                return redirect('home')

            # Update user information in Keycloak
            user_id = existing_users[0]['id']
            keycloak_admin.update_user(user_id, {
                'firstName': data.get('first_name'),
                'lastName': data.get('last_name'),
                'email': data.get('email'),
            })

            messages.success(request, 'Your profile has been successfully updated.')
            return redirect('home')
    else:
        # Get the user in Django's database
        try:
            django_user = CustomUser.objects.get(email=request.user.email)
        except User.DoesNotExist:
            messages.error(request, 'User not found in Django database.')
            return redirect('home')

        # Load the current user information from Django database
        initial_data = {
            'first_name': django_user.first_name,
            'last_name': django_user.last_name,
            'email': django_user.email,
            'address': django_user.address,  # assuming you have these fields in form
            'phone': django_user.phone,  # assuming you have these fields in form
            # ... add any other fields you have in your form and model
        }
        form = UserProfileForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'update_profile.html', context)
