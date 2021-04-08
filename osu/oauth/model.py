from pydantic import BaseModel


class ClientCredentialModel(BaseModel):
    token_type: str
    expires_in: int
    access_token: str


__all__ = ["ClientCredentialModel"]
