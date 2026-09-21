import jwt
from datetime import datetime, timezone
import datetime as dt

public_key = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA6UhPOeHLtipyVzcCn/eF
UcWg/N/4AxSA2OjqnR0wIUWEIVJWgsvmOtcStGbKcqMg0wi39JUV+9EGIdJCBqHc
88RHJD/xwX4ca/Pcs1A+0B08Y9VF4JoMOQSudw+DBMEsI87kYRhZiEE4CslvPVOr
DpTdaA+2GlqCuZYLnz3l3BzOWnYw3fPm8YnL3VAan3iVjvY9eP54LT44sVUZgMnQ
nb2jjv8RPHOt8eo+01MkptwCaWgnnM7qMsClltg0R5nwiVY9zpQEI6lldgVPKL1/
CwZPI7ymHCibF+o3ij3qfZAaTIBwmc4QTeC46KNP0B4RdUPrj6/mmJlxnM1nAdGW
aQIDAQAB
-----END PUBLIC KEY-----
"""

private_key = """
-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDpSE854cu2KnJX
NwKf94VRxaD83/gDFIDY6OqdHTAhRYQhUlaCy+Y61xK0ZspyoyDTCLf0lRX70QYh
0kIGodzzxEckP/HBfhxr89yzUD7QHTxj1UXgmgw5BK53D4MEwSwjzuRhGFmIQTgK
yW89U6sOlN1oD7YaWoK5lgufPeXcHM5adjDd8+bxicvdUBqfeJWO9j14/ngtPjix
VRmAydCdvaOO/xE8c63x6j7TUySm3AJpaCeczuoywKWW2DRHmfCJVj3OlAQjqWV2
BU8ovX8LBk8jvKYcKJsX6jeKPep9kBpMgHCZzhBN4Ljoo0/QHhF1Q+uPr+aYmXGc
zWcB0ZZpAgMBAAECgf89wT/nClNJ5Fsge2cgltarwzSmryOfTsyDCzMd/AmNgeIA
9u5shdRrGhvsB4a1XFS+RZxfhkckz94o95YNE9ZydO1ZlWTAOu4R7/Qc2337OC3h
EKAtQn+RaWNufDiIxKE2geslz7MZxZXi5tHyl6ENfNDwr3tvsRBL0NN1UqGxAsVP
iek60HSZl1g4MU4V1tytv3+2LHmuhcGqO0l8er6+ZXTXreZ413y/0Bdp/VNHt+7T
S/yIFaEY2p5mXx8Yok5Ce80SDBbkPowpJzx8MPYERk6iWhtCiaxBHxpoDZkiBIuV
M3fTqTXow38MZFFRJSmUz+GmjY3gtaObG8uA3pECgYEA+1lfRCYg/XWPFVIE22iT
HX5nL1r9k4GvG1vRsKL1Wdjs1gY7zB5BYph9HvDbkHgNogE3ZuBTEZh2aIcgOQZt
7tlBX6659ZuELmRCBjupQh/L+O18qSC/MCGuaPEQ0pK3ZCDRW8JxY9rTd1E8VcRM
27fQBH3D51Rrwkus/CnQZhkCgYEA7ZlbRl0oX8fM5YiX+MDNKfYl22XLgD4ei32R
59UYG114C8fruz0955kBxPBzcanhrU6lBnkQ2OLSTsqEiCNBGoTQnkyP3bSJpfgt
ZOI4GqIEwBPmW4soQupJRKnuuO0qy7XM3FJ2miRE2+lKG5PsOi2U8oTPz8/xlC4R
wa0PnNECgYAHXBuVBETNByc0aZ1oy0wbffsJgPGR4yc8dtjSAkOK6PYuYipYFL63
Y12ujUDwnwNPLhfwNDtadYtqDiLcaJrJdqUaZyRc07vwG9FvG0oefI3dcR7IWQQg
JaxUuFJUyCUEko1u0We+k8bDZKaOoFvbxysZJpGY8XjiTJL5I0RN6QKBgQC2hnsy
ANrFSc5D/r0Qobx6odfPRdIhgJcifaKawH82doWEN18GhjOKOWa8jiOBjAoMg0AP
Su4AT69UTAuoMb0PzDwff519qfWchJ0KxSZof1K65A6xAKQ7U5RZpVn4wml/+PeZ
wdfO7lHfxsXhja+Juf6UmCa09IAXX5TQfkxiIQKBgQDoiBBJmqCXBAYPRuaCuKcJ
137hBh7EhoYOdtVp+C8oPd8+AtpLxA016NZeIRwM6G/vWSEuObXcsdqHm1NgZO5t
3GrcNVl1sK3a4L335xsujrYA/kKLSbVvxXM3vWiTbzTVyNQPapLLslamCin7fYL7
tWJnDDtKRrSElNZ1TdIfSg==
-----END PRIVATE KEY-----
"""

# with open("keys/public.pem", "r") as file:
#     public_key = file.read()

# with open("keys/private.pem", "r") as file:
#     private_key = file.read()

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