import requests
import hashlib
import base64

CLIENT_ID = "lsqateam@gmail.com"
CLIENT_SECRET = "Abc123!!"

REDIRECT_URI = "http://postman.com"
AUTHORIZE_URL = "https://powerfox-identity-web-app-dev.azurewebsites.net/connect/authorize"
ACCESS_TOKEN_URL = "https://powerfox-identity-web-app-dev.azurewebsites.net/connect/token"
USER = 'lsqateam@gmail.com:Abc123!!'
#CODE_CHALENGE = base64.b64encode(hashlib.sha256(USER.encode('utf-8')).digest())
CODE_CHALENGE = 'kNGKnChpy-VXCM0XDrgDNohW4njlwhv4fmmdre-s-hM'
# Get authorization code
a = requests.get('{}?response_type=code&client_id={}&scope=api&redirect_uri={}&code_challenge={}&code_challenge_method=S256'.format(AUTHORIZE_URL, CLIENT_ID, REDIRECT_URI, CODE_CHALENGE))


# Get access token
b = requests.post(
    ACCESS_TOKEN_URL,
    data={
        'grant_type': 'authorization_code',
        'code': '19BAEE30DBF9768C79EB8DC65BCDA77C705D4C99EDA2F831BD74BB636167E9FA-1',
        'code_verifier': '4IVfWSqmZ96td0zjBT7svASmfIvLLdMvPLXlG9i5n1U',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI
    }
)
print(b.json())

# # Execute another request using accesss token
# requests.get('https://sketchfab.com/v2/users/me', headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN'})
#
# # Get refresh token
# requests.post(
#     ACCESS_TOKEN_URL,
#     data={
#         'grant_type': 'refresh_token',
#         'client_id': CLIENT_ID,
#         'client_secret': CLIENT_SECRET,
#         'refresh_token': 'YOUR_REFRESH_TOKEN'
#     }
# )
