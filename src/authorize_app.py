import requests
from requests.auth import HTTPBasicAuth
  
import user_credentials

consumer_key = user_credentials.consumer_key
consumer_secret = user_credentials.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

j_response = r.json()

access_token = j_response['access_token']