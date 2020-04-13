import  requests
from requests.auth import HTTPBasicAuth

import user_credentials


#Authenticate Application

def authenticate_application():
    consumer_key = user_credentials.consumer_key
    consumer_secret = user_credentials.consumer_secret


    auth_request = requests.get(user_credentials.authentication_api_URL, auth=HTTPBasicAuth(user_credentials.consumer_key, user_credentials.consumer_secret))

    authrequest_jsonresponse = auth_request.json()

    access_token = authrequest_jsonresponse['access_token']

    return str.format(access_token)
    