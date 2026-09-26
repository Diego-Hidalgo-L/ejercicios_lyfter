import jwt
from datetime import datetime, timezone
import datetime as dt

with open("keys/public.pem", "r") as file:
    public_key = file.read()

with open("keys/private.pem", "r") as file:
    private_key = file.read()

# Se encarga de crear los tokens
class JWTManager:
    def __init__(self, public_key=public_key, private_key=private_key, algorithm="RS256"):
        self.public_key = public_key
        self.private_key = private_key
        self.algorithm = algorithm

    def encode(self, user_id, token_type):
        try:
            if token_type not in ["access", "refresh"]:
                raise ValueError("Invalid token type")

            if token_type == "access":
                exp = datetime.now(tz=timezone.utc) + dt.timedelta(minutes=15)

            elif token_type == "refresh":
                exp = datetime.now(tz=timezone.utc) + dt.timedelta(days=7)

            payload = {"id":user_id, "token_type":token_type, "exp":exp}
            encoded = jwt.encode(payload, self.private_key, algorithm=self.algorithm)

            return encoded

        except ValueError as error:
            print(error)
            return None
        
        except Exception as error:
            print(error)
            return None

    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.public_key, algorithms=[self.algorithm])
            return decoded
        
        except Exception as error:
            print(error)
            return None