from farcaster import Warpcast

class Authenticator:
    def __init__(self, access_token=None):
        self.access_token = access_token

    def authenticate(self):
        return Warpcast(access_token=self.access_token) if self.access_token else None
