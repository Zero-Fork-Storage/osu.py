import requests
from osu.oauth.model import ClientCredentialModel


class AuthorizationError(Exception):
    pass


class ClientCredentials:
    def __init__(
            self,
            client_id: int,
            client_secret: str,
            grant_type: str = "client_credentials",
            scope: str = "public"
    ) -> None:
        """osu.py


        Client Credentials Grant
        ========================
        ------------------------

        The client credential flow provides a way for developers to get access tokens that do not have associated
        user permissions; as such, these tokens are considered as guest users.


        :param client_id: The Client ID you received when you registered
        :param client_secret: The client secret of your application.
        :param grant_type: This must always be `client_credentials`
        :param scope: Must be `public`; other scopes have no meaningful effect.
        """

        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type
        self.scope = scope

        self.url = "https://osu.ppy.sh/oauth/token"
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def get_access_token(self) -> ClientCredentialModel:
        query = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": self.grant_type,
            "scope": self.scope
        }
        req = requests.post(
            url=self.url,
            json=query,
            headers=self.headers
        )
        if req.status_code != 200:
            raise AuthorizationError(f"HTTP CODE: {req.status_code}")

        response_data = req.json()
        return ClientCredentialModel(**response_data)
