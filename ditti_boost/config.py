from farcaster import Warpcast
from dotenv import load_dotenv
import os

class Authenticator:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file
        self.access_token = os.getenv('ACCESS_TOKEN') or self.prompt_for_credentials()

    def authenticate(self):
        if self.access_token:
            return Warpcast(access_token=self.access_token)
        else:
            raise ValueError("Access token is required for authentication.")

    def save_credentials_to_env(self, access_token):
        with open('.env', 'w') as env_file:
            if access_token:
                env_file.write(f"ACCESS_TOKEN={access_token}\n")

    def prompt_for_credentials(self):
        access_token_input = input("Please enter an access token: ").strip()
        if not access_token_input:
            print("Error: Access token is empty.")
            exit(1)

        self.save_credentials_to_env(access_token_input)
        return access_token_input
