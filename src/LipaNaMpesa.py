import requests
import authorize_app
import user_credentials

access_token = authorize_app.access_token
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

header = {"Authorization": "Bearer %s" %access_token}


request = {
            "BusinessShortCode": user_credentials.business_shortCode,
            "Password": user_credentials.generate_password,
            "Timestamp": user_credentials.generate_timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": user_credentials.transaction_amount,
            "PartyA": user_credentials.party_A,
            "PartyB": user_credentials.business_shortCode,
            "PhoneNumber": user_credentials.party_A,
            "CallBackURL": "https://ip_address:port/callback",
            "AccountReference": user_credentials.account_reference,
            "TransactionDesc": user_credentials.transaction_description
    }

response = requests.post(api_url, json=request, headers=header)

print(response.text)

