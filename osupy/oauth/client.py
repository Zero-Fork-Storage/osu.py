import requests

from pydantic import BaseModel


class ClientAccessTokenInterface(BaseModel):
    token_type: str
    expires_in: int
    access_token: str


class ClientAuthorization:
    """Client Credentials Grant

        The client credential flow provides a way for developers to 
        as such, these tokens are considered as guest users.
    """
    def __init__(self, client_id: int, client_secret: str, grant_type: str, scope: str) -> None:
        """
        :param int client_id: Client ID you received when you registered.
        :param str client_secret: Client secret of your application.
        :param str grant_type: This must always be client_credentials.
        :param str scope: Must be public other scopes have no meaningful effect.
        """
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type
        self.scope = scope

    
    def get_access_token(self) -> ClientAccessTokenInterface:
        body = {
            'grant_type': self.grant_type,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': self.scope
        }
        resp = requests.post(
            url="https://osu.ppy.sh/oauth/token",
            headers=self.headers,
            json=body
        )
        if resp.status_code != 200:
            print(resp.status_code)
            raise Exception

        res = resp.json()
        credentials = ClientAccessTokenInterface(**res)
        return credentials.json()
