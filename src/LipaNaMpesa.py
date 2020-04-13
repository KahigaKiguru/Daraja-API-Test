import requests
from requests.auth import HTTPBasicAuth
import base64
from datetime import datetime

import user_credentials
import authenticate_app

#Generate timestamp

timestamp =  datetime.now().strftime("%Y%m%d%H%M%S")

# Generate password

credentials_to_encode = user_credentials.business_shortCode + user_credentials.lipa_na_mpesa_passkey + timestamp
encoded_password = base64.b64encode(credentials_to_encode.encode())
decoded_password = encoded_password.decode("utf-8")






# Prepare and Send Transaction Request


header = {"Authorization": "Bearer %s" %authenticate_app.access_token}


request = {
            "BusinessShortCode": user_credentials.business_shortCode,
            "Password": decoded_password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": user_credentials.transaction_amount,
            "PartyA": user_credentials.party_A,
            "PartyB": user_credentials.business_shortCode,
            "PhoneNumber": user_credentials.party_A,
            "CallBackURL": "https://enzitechnologies.com/callbacks/url",
            "AccountReference": user_credentials.account_reference,
            "TransactionDesc": user_credentials.transaction_description
    }

response = requests.post(user_credentials.processrequest_api_url, json=request, headers=header)

print(response.text)

