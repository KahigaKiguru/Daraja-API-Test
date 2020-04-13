import authenticate_app
import user_credentials
import requests

access_token = authenticate_app.access_token
api_url = user_credentials.register_api_url
headers = {"Authorization": "Bearer %s" % access_token}

request = { 
            "ShortCode": user_credentials.business_shortCode,
            "ResponseType": " ",
            "ConfirmationURL": user_credentials.confirmation_url,
            "ValidationURL": user_credentials.validation_url
    }

response = requests.post(api_url, json = request, headers=headers)

print (response.text)