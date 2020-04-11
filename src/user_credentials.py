import base64
from datetime import datetime 

import user_credentials


business_shortCode = "174379"
lipa_na_mpesa_passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
timestamp =  datetime.now().strftime("%Y%m%d%H%M%S")
transaction_amount = "5"
party_A = "254768368538"
party_B = business_shortCode
transaction_description = "This is a test transaction"

consumer_key = "Ao3QYU37kN6QnNKAA3Ja6lga9Qu8qLdi"
consumer_secret = "mqluVXHBt5SA9xyz"

def generate_password():
    credentials_to_encode = business_shortCode + lipa_na_mpesa_passkey + timestamp

    encoded_password = base64.b64encode(credentials_to_encode.encode())
    decoded_password = encoded_password.decode("utf-8")
    
    return decoded_password

def generate_timestamp():

    timestamp =  datetime.now().strftime("%Y%m%d%H%M%S")

    return timestamp

def account_reference():
    return 54865465