import pyotp
from project_b.settings import ACCOUNT_SID,AUTH_TOKEN,FROM_MOBILE_NUMBER
from twilio.rest import Client
def generateOtp():
    secret_key = pyotp.random_base32()
    totp = pyotp.TOTP(secret_key)
    otp = totp.now()
    return otp
def  sendMsg(mobile,msg):
    client = Client(ACCOUNT_SID,AUTH_TOKEN)
    message = client.messages.create(
        from_=FROM_MOBILE_NUMBER,
        body=msg,
        to=mobile
    )
    print(message.sid)
def addVerifiedNumber(mobile,name):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    verification = client.validation_requests.create(mobile, friendly_name=name)
    print(verification.status)

