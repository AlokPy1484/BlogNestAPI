import requests
from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError
from rest_framework import authentication, exceptions

from django.conf import settings

class ClerkAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return None

        token = auth_header.split(" ")[1]

        try:
            jwks = requests.get(settings.CLERK_JWKS_URL).json()
            unverified_header = jwt.get_unverified_header(token)
            key = next(
                (k for k in jwks["keys"] if k["kid"] == unverified_header["kid"]), None
            )
            if key is None:
                raise exceptions.AuthenticationFailed("Invalid token key ID")

            payload = jwt.decode(
                token,
                key,
                algorithms=["RS256"],
                audience=None,  # Clerk tokens often don't require audience validation
                issuer=settings.CLERK_ISSUER,
                options={"verify_aud": False}
            )

        except ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Token expired")
        except JWTError as e:
            raise exceptions.AuthenticationFailed(f"Token invalid: {str(e)}")
        
        decoded = jwt.get_unverified_claims(token)
        # You can now access user info from payload
        print("Decoded payload:", payload)
        clerk_user_id = payload.get("sub")
        clerk_user_name = payload.get("username")
        # username = payload.get("username") 
        #  

        # print(decoded)
        # full_name = decoded.get("name")
        # email = payload.get("email_address")
        # username = email.split('@')[0]

        # email = payload.get("email")


        response = requests.get(
            f"https://api.clerk.dev/v1/users/{clerk_user_id}",
            headers={"Authorization": f"Bearer {settings.CLERK_SECRET_KEY}"}
        )
        if response.status_code == 200:
            data = response.json()
            email = data["email_addresses"][0]["email_address"]
            username = data.get("username") or email.split("@")[0]
            print(f"USERNAME is -------> {username}")
        else:
            raise Exception("Could not fetch user data from Clerk")





        # Optionally, create or get local user
        from django.contrib.auth.models import User
        user, _ = User.objects.get_or_create(username=username)

        return (user, None)








