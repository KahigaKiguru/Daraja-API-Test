import authenticate_app
import user_credentials
import requests

def register_url():
    access_token = authenticate_app.access_token
    api_url = user_credentials.register_api_url
    headers = {"Authorization": "Bearer %s" %access_token}

    request = { 
                "ShortCode": user_credentials.shortcode_1,
                "ResponseType": "Confirmed",
                "ConfirmationURL": user_credentials.confirmation_url,
                "ValidationURL": user_credentials.validation_url
        }

    response = requests.post(api_url, json = request, headers=headers)

    
def simulate_c2bTransaction():
  access_token = authenticate_app.authenticate_application()
  api_url = user_credentials.c2b_simulate_url
  headers = {"Authorization": "Bearer %s" % access_token}
  request = { "ShortCode": user_credentials.shortcode_1,
    "CommandID":"CustomerPayBillOnline",
    "Amount": user_credentials.transaction_amount,
    "Msisdn": user_credentials.test_msisdn,
    "BillRefNumber": user_credentials.account_reference
     }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)
  
simulate_c2bTransaction()