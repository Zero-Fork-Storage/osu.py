import os

from osu.oauth import ClientCredentials
from osu.oauth.model import ClientCredentialModel

try:
    client_id: int = int(os.environ.get("CLIENT_ID"))
    client_secret: str = os.environ.get("CLIENT_SECRET")
except TypeError as e:
    raise e


def test_get_client_credentials():
    credentials_obj = ClientCredentials(
        client_id=client_id, client_secret=client_secret
    )
    credential = credentials_obj.get_access_token()
    assert ClientCredentialModel(**credential.dict())
