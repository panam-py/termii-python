import requests
import json

SEND_TOKEN_URL = 'https://api.ng.termii.com/api/sms/otp/send'
SEND_TOKEN_VOICE_URL = "https://api.ng.termii.com/api/sms/otp/send/voice"
SEND_TOKEN_VOICECALL_URL = "https://api.ng.termii.com/api/sms/otp/send/voice"

def send_token(api_key, message_type, phone_number, 
        sender_id, channel, pin_attempts, pin_time_to_live,
        pin_length, pin_placeholder, message_text, pin_type,):
    """
    Function that allows businesses generate a one-time-passwords(OTP).
    It happens across every channel on Termii.
    They are generated randomly and can be set to expire within a time-frame

    Parameters:
    api_key : string
        API key for Termii account.
    message_type : ALPHANUMERIC / NUMERIC
        Dynamic string that will be sent as part of OTP message.
    phone_number : integer
        The destination number of the client receiving the OTP message.
        Number must be in international format.
    sender_id : string
        ID of the sender of the OTP.
    channel : string
        Dynamic string route through which the OTP message is sent.
        Can be set to dnd or Whatsapp or generic.
    pin_attempts : ALPHANUMERIC / NUMERIC
        PIN code that is generated and sent with the OTP message.
        Has a minimum of one attempt.
    pin_time_to_live : integer
        Represents time of PIN validation before expiry.
        Time is in minutes and has a minimum of 0 and maximum of 60.
    pin_length : integer
        Length of PIN code. Has a minimum of 4 and maximum of 8.
    pin_placeholder : string
        Before sending the OTP message, the PIN placeholder is replaced with
        generic pin code.
    message_text : string
        Message text that would be sent to destination phone number.
    """
    payload = {
        'api_key' : api_key,
        message_type : 'NUMERIC',
        'to' : phone_number,
        'from' : sender_id,
        channel : 'generic',
        pin_attempts : 10,
        pin_time_to_live : 1,
        pin_length : 6,
        pin_placeholder : '< 1234 >',
        message_text : 'Your pin is < 1234 >',
        pin_type : 'NUMERIC',
    }
    
    headers = {
        'Content-Type' : 'application/json',
    }

    response = requests.post(SEND_TOKEN_URL, headers=headers, json=payload)
    return response


def voice_token(api_key, phone_number, pin_attempts, 
                pin_time_to_live, pin_length):
    """
    Function that enables you to generate and trigger one-time-passwords
    via a voice channel to a phone number. OTPs are generated and sent to
    phone numbers and can only be verified using Verify Token function.

    Parameters:
    api_key : string
        API key for Termii account.
    phone_number : integer
        The destination number of the client receiving the voice token.
        Number must be in international format.
    pin_attempts : NUMERIC / ALPHANUMERIC
        PIN code that is generated and sent with the OTP message.
        Has a minimum of one attempt.
    pin_time_to_live : integer
        Represents time of pin validation before expiry.
        Time is in minutes and has a minimum of 0 and maximum of 60.
    pin_length : integer
        Length of PIN code. Has a minimum of 4 and maximum of 8.
    """
    payload = {
        'api_key' : api_key,
        'from' : phone_number,
        pin_attempts : 10,
        pin_time_to_live : 5,
        pin_length : 6,  
    }
    
    headers = {
        'Content-type' : 'application/json',
    }
    
    response = requests.post(SEND_TOKEN_VOICE_URL, headers=headers, json=payload)
    return response


def voice_call(api_key, phone_number, code):
    payload = {
        'api_key' : api_key,
        'to' : phone_number,
        'code' : code,
    }
    
    headers = {
        'Content-type' : 'application/json',
    }
    
    response = requests.post(SEND_TOKEN_VOICECALL_URL, headers=headers, json=payload)
    return response