import requests
import urllib.parse

class WebAuthorization:
    def __init__(self, client_id: int, client_secret: str, grant_type: str, redirect_uri: str):
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type
        self.redirect_uri = redirect_uri

    def generate_authorization_url(self):
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "code",
            "scope": "public",
            "state": "daddasdads"
        }
        a = urllib.parse.urlencode(params)
        print("https://osu.ppy.sh/oauth/authorize?"+a)
    def get_access_token(self):
        body = {
            "grant_type": self.grant_type,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
            "code": "code"
        }
        print(body)
        resp = requests.post(
            url="https://osu.ppy.sh/oauth/authorize",
            headers=self.headers,
            data=body
        )
        if resp.status_code != 200:
            print(resp.status_code)
            print(resp.content)
            raise Exception

        return resp.content
