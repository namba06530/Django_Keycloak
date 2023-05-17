# Classes to override default OIDCAuthenticationBackend (Keycloak authentication)
from django.http import HttpResponseRedirect
from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from urllib.parse import urlencode
import requests
from jose import jwt
from jose.exceptions import JWTError
from .utils.keycloak_common import server_url, realm_name, client_id, redirect_uri, client_secret_key
from .models import CustomUser


class KeycloakOIDCAuthenticationBackend(OIDCAuthenticationBackend):

    def authenticate_keycloak(self, request):
        # Rediriger l'utilisateur vers Keycloak pour l'authentification
        auth_url = f"{server_url}realms/{realm_name}/protocol/openid-connect/auth"
        query_params = {
            'client_id': client_id,
            'redirect_uri': redirect_uri,
            'response_type': 'code',
            'scope': 'openid',
            'prompt': 'login',
        }
        return HttpResponseRedirect(auth_url + '?' + urlencode(query_params))

    def otp_callback(self, request):
        # Cette fonction est appelée quand Keycloak redirige l'utilisateur vers votre application
        auth_code = request.GET.get('code')

        # Échanger le code d'autorisation pour un jeton d'accès
        token_url = f"{server_url}realms/{realm_name}/protocol/openid-connect/token"
        data = {
            'grant_type': 'authorization_code',
            'client_id': client_id,
            'client_secret': client_secret_key,
            'code': auth_code,
            'redirect_uri': redirect_uri,
        }
        response = requests.post(token_url, data=data)
        if response.status_code == 200:  # Si le code d'autorisation est correct
            token_data = response.json()
            id_token = token_data['id_token']
            access_token = token_data['access_token']
            claims = self.decode_jwt(id_token, audience=client_id)

            user = self.get_or_create_user(id_token=id_token, access_token=access_token, payload=claims)
            return user

            # Continuer avec votre logique d'authentification

        else:  # Si le code d'autorisation est incorrect
            print(f"CODE D'AUTORISATION INCORRECT")
            return None

    def create_user(self, claims):
        user = super().create_user(claims)
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.email = claims.get('email')
        user.username = claims.get('preferred_username')
        user.keycloak_id = claims.get('sub')  # The 'sub' claim contains the Keycloak user ID
        user.email_verified = claims.get('email_verified', False)  # Update email_verified field
        user.save()
        return user

    def update_user(self, user, claims):
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.email = claims.get('email')
        user.username = claims.get('preferred_username')
        user.keycloak_id = claims.get('sub')  # The 'sub' claim contains the Keycloak user ID
        user.email_verified = claims.get('email_verified', False)  # Update email_verified field
        user.save()
        return user

    def filter_users_by_claims(self, claims):
        keycloak_id = claims.get('sub')

        if not keycloak_id:
            return self.UserModel.objects.none()

        return self.UserModel.objects.filter(keycloak_id=keycloak_id)

    def decode_jwt(self, token, audience):
        try:
            # Fetch the JWKS from Keycloak
            jwks_url = f"{server_url}realms/{realm_name}/protocol/openid-connect/certs"
            response = requests.get(jwks_url)
            jwks = response.json()

            # Extract the header from the JWT
            header = jwt.get_unverified_header(token)

            # Find the proper key from the JWKS using the 'kid' from the header
            key = None
            for jwk_key in jwks['keys']:
                if jwk_key['kid'] == header['kid']:
                    key = jwk_key
                    break

            if key is None:
                raise ValueError("No matching key found in JWKS")

            # Decode the JWT using the key
            decoded_token = jwt.decode(token, key, algorithms=['RS256'], audience=audience)
            return decoded_token

        except JWTError as e:
            return None
