import requests
import json
from .utils.keycloak_common import server_url, client_id, realm_name, client_secret_key
from keycloak import KeycloakAdmin, KeycloakOpenID, KeycloakOpenIDConnection

# Configure the Keycloak OpenID client
keycloak_openid = KeycloakOpenID(
    server_url=server_url,
    client_id=client_id,
    realm_name=realm_name,
    client_secret_key=client_secret_key,
    verify=True)

# Create an instance of the Keycloak Admin API client
keycloak_connection = KeycloakOpenIDConnection(
    server_url=server_url,
    client_id=client_id,
    realm_name=realm_name,
    client_secret_key=client_secret_key,
    verify=True)

keycloak_admin = KeycloakAdmin(connection=keycloak_connection, server_url=server_url)


def get_access_token():
    token_url = f"{server_url}realms/{realm_name}/protocol/openid-connect/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret_key
    }
    response = requests.post(token_url, data=payload)
    response_data = json.loads(response.text)
    access_token = response_data['access_token']
    return access_token
