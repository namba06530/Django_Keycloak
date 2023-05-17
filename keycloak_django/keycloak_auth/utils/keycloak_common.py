from django.conf import settings

server_url = settings.OIDC_OP_BASE_URL
client_id = settings.OIDC_RP_CLIENT_ID
realm_name = settings.OIDC_RP_REALM_NAME
client_secret_key = settings.OIDC_RP_CLIENT_SECRET
admin_username = settings.OIDC_DEV_ADMIN_USERNAME
admin_password = settings.OIDC_DEV_ADMIN_PASSWORD
email_sender_address = settings.EMAIL_HOST_USER
redirect_uri = settings.REDIRECT_URI
logout_endpoint = settings.OIDC_OP_LOGOUT_ENDPOINT
keycloak_backend = 'keycloak_auth.auth.KeycloakOIDCAuthenticationBackend'
realm_url = f"{server_url}admin/realms/{realm_name}"

