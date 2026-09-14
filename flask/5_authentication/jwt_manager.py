import jwt

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

    def encode(self, data):
        try:
            encoded = jwt.encode(data, self.private_key, algorithm=self.algorithm)
            return encoded
        except Exception as error:
            print(error)
            return None

    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.public_key, algorithms=[self.algorithm])
            return decoded
        except Exception as e:
            print(e)
            return None