import requests
import json
from utilities import WrongMediaOptions, WrongType

FETCH_SENDER_ID_URL = "https://api.ng.termii.com/api/sender-id"
REQUEST_SENDER_ID_URL = "https://api.ng.termii.com/api/sender-id/request"
SEND_MESSAGE_URL = "https://api.ng.termii.com/api/sms/send"
BULK_MESSAGE_URL = "https://api.ng.termii.com/api/sms/send/bulk"
NUMBER_MESSAGE_SEND_URL = "https://api.ng.termii.com/api/sms/number/send"
DEVICE_TEMPLATE_URL = "https://api.ng.termii.com/api/send/template"
PHONEBOOKS_URL = "https://api.ng.termii.com/api/phonebooks"
DELETE_CONTACT_URL = "https://api.ng.termii.com/api/phonebook/contact"

def get_sender_ids(api_key):
    """
    Fetches sender ids associated with an API key from the termii API.

    Params:
    api_key: str
        The API key for a certain termii account
    """
    response = requests.get(f"{FETCH_SENDER_ID_URL}?api_key={api_key}")
    response = json.loads(response.content)
    return response

def request_new_sender_id(api_key, sender_id, usecase, company):
    """
    Simple function to request new termii sender ID.

    Params:
    api_key: str
        The API key for a certain termii account
    sender_id: str
        The name of the new sender_id to create
    usecase: str
        The usecase of the new sender_id
    company: str
        The name of the company associated with this sender_id
    """
    payload = {
         "api_key":api_key,
         "sender_id": sender_id,
         "usecase": usecase,
         "company": company
    }

    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.post(REQUEST_SENDER_ID_URL, json=payload, headers=headers)
    response = json.loads(response.content)
    return response

def post_message(api_key, number_to, sender_id, message, message_type, channel, media_dict):
    """
    Function to send a message using the termii API.

    Params:
    api_key: str
        The API key for a certain termii account
    number_to: str
        The phone number the message should be sent to in international format. '+' should be excluded
    sender_id: str
        The sender id this message should be sent from and identify with
    message: str
        The message to be sent.
    message_type: str
        The type of message to be sent. Should be 'plain'
    channel: str
        The channel this message should be sent with. Can be 'dnd', 'whatsapp' or 'generic'
    media_dict: dict
        A dictionary containing the options for media if applicable. Should contain 'url' and 'caption' keys. Pass an empty dictionary if not applicable
    """

    if type(media_dict) != dict:
        raise WrongType("dict", "media_dict")

    if len(media_dict.keys()) > 0:
        if 'url' in media_dict.keys() and 'caption' in media_dict.keys():
            payload = {
                "to": number_to,
                "from": sender_id,
                "sms": message,
                "type": message_type,
                "channel": channel,
                "api_key": api_key,
                "media": {
                        "url": media_dict["url"],
                        "caption": media_dict["caption"]
                    }   
            }
        else:
            raise WrongMediaOptions()
    else:
        payload = {
                "to": number_to,
                "from": sender_id,
                "sms": message,
                "type": message_type,
                "channel": channel,
                "api_key": api_key,
        }
    
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.post(SEND_MESSAGE_URL, json=payload, headers=headers)
    response = json.loads(response.content)
    return response

def post_message_bulk(api_key, numbers_to, sender_id, message, message_type, channel):
    """
    Function to send a bulk message using the termii API.

    Params:
    api_key: str
        The API key for a certain termii account
    numbers_to: str
        An array containing the phone numbers the message should be sent to in international format. '+' should be excluded
    sender_id: str
        The sender id this message should be sent from and identify with
    message: str
        The message to be sent.
    message_type: str
        The type of message to be sent. Should be 'plain'
    channel: str
        The channel this message should be sent with. Can be 'dnd', 'whatsapp' or 'generic'
    """

    if type(numbers_to) != list:
        raise WrongType("list", "numbers_to")

    payload = {
          "to": numbers_to,
           "from": sender_id,
           "sms": message,
           "type": message_type,
           "channel": channel,
           "api_key": api_key,
    }

    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.post(BULK_MESSAGE_URL, json=payload, headers=headers)
    response = json.loads(response.content)
    return response

def number_message_send(api_key, number_to, message):
    """
    Function to send messages to customers using Termii's auto-generated messaging numbers that adapt to customers location.

    Params:
    api_key: str
        The API key for a certain termii account
    number_to: str
        The phone number the message should be sent to in international format. '+' should be excluded
    message: str
        The message to be sent.
    """
    payload = {
           "to": number_to,
           "sms": message,
           "api_key": api_key
    }

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.post(NUMBER_MESSAGE_SEND_URL, json=payload, headers=headers)
    response = json.loads(response.content)
    return response

def template_setter(api_key, phone_number, device_id, template_id, data):
    """
    A function to set a device template for the one-time-passwords (pins) sent to their customers via whatsapp or sms.

    Params:
    api_key: str
        The API key for a certain termii account
    phone_number: str
        The destination phone number. Phone number must be in the international format without '+'
    device_id: str
        Represents the Device ID for Whatsapp. It can be Alphanumeric. It should be passed when the message is sent via whatsapp (It can be found on the manage device page on your Termii dashboard)
    template_id: str
        The ID of the template used
    data: dict
        Represents an object of key: value pair. The keys for the data object can be found on the device subscription page on your dashboard.
    """

    if type(data) != dict:
        raise WrongType("dict", "data")
    
    payload = {
        "phone_number": phone_number,
        "device_id": device_id,
        "template_id": template_id,
        "api_key": api_key,
        "data":data
    }

    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.post(DEVICE_TEMPLATE_URL, headers=headers, json=payload)
    response = json.loads(response.content)
    return response

def get_phonebooks(api_key):
    """
    A function to get all the phonebooks associated to a termii client

    Params:
    api_key: str
        The API key for a certain termii account
    """

    response = requests.get(f"{PHONEBOOKS_URL}?api_key={api_key}")
    response = json.loads(response.content)
    return response

def make_phonebook(api_key, description, phonebook_name):
    """
    Function to create a phonebook using the termii API

    Params:
    api_key: str
        The API key for a certain termii account
    description: str
        A description of the contacts stored in the phonebook
    phonebook_name: str
        The name of the phonebook
    """

    payload = {
        "api_key": api_key,
        "phonebook_name": phonebook_name,
        "description": description
    }

    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.post(PHONEBOOKS_URL, json=payload, headers=headers)
    response = json.loads(response.content)
    return response

def patch_phonebook(api_key, phonebook_id, phonebook_name, phonebook_description):
    """
    Function to create a phonebook using the termii API

    Params:
    api_key: str
        The API key for a certain termii account
    phonebook_id: str
        The id of the phonebook to be updated
    phonebook_name: str
        The name of the phonebook
    phonebook_description: str
        The description of the phonebbok
    """
    payload = {
        "api_key": api_key,
        "phonebook_name": phonebook_name,
        "description": phonebook_description
    }

    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.patch(url=f"{PHONEBOOKS_URL}/{phonebook_id}", json=payload, headers=headers)
    response = json.loads(response.content)
    return response

def remove_phonebook(api_key, phonebook_id):
    """
    Function to delete a phonebook using the termii API

    Params:
    api_key: str
        The API key for a certain termii account
    phonebook_id: str
        The id of the phonebook to be updated
    """

    response = requests.delete(url=f"{PHONEBOOKS_URL}/{phonebook_id}?api_key={api_key}")
    response = json.loads(response.content)
    return response

def get_contacts_from_phonebook(api_key, phonebook_id):
    """
    A function to get all the contacts associated to a termii phonebook

   Params:
    api_key: str
        The API key for a certain termii account
    phonebook_id: str
        The id of the phonebook
    """
    response = requests.get(url=f"{PHONEBOOKS_URL}/{phonebook_id}/contacts?api_key={api_key}")
    response = json.loads(response.content)
    return response

def add_contact(api_key, phone_number, phonebook_id, options):
    """
    A function to add a single contact to a phonebook using the termii API

    Params:
    api_key: str
        The API key for a certain termii account
    phone_number: str
        Phone number of the contact without international format.
    phonebook_id: str
        The id of the phonebook
    options: dict
        A dictionary containing certain options such as 'country_code', 'email_address', 'first_name', 'last_name' and 'company' which are all strings. An empty dictionary should be passed if there are no options.
    """

    if type(options) != dict:
        raise WrongType("dict", "options")
    
    payload = {
        "api_key": api_key,
        "phone_number": phone_number
    }

    for option in options.keys():
        if option == "country_code" or option == "email_address" or option == "first_name" or option == "last_name" or option == "company":
            payload[option] = options[option]
        
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.post(url=f"{PHONEBOOKS_URL}/{phonebook_id}/contacts")
    response = json.loads(response.content)
    return response

def add_many_contacts(api_key, contact_file, country_code, extension, phonebook_id):
    """
    A function to add contacts to a phonebook using the termii API

    Params:
    api_key: str
        The API key for a certain termii account
    contact_file: str
        File containing the list of contacts you want to add to your phonebook. Supported files include : 'txt', 'xlsx', and 'csv'.
    country_code: str
        Represents short numeric geographical codes developed to represent countries (Example: 234 ).
    extension: str
        The extension of the contact file: (Example: 'text/csv')
    phonebook_id: str
        The id of the phonebook
    """

    payload={'country_code': country_code}

    files= [(country_code, (contact_file, 'rb'), extension)]

    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.post(url=f"{PHONEBOOKS_URL}/{phonebook_id}/contacts?api_key={api_key}", json=payload, files=files, headers=headers)
    response = json.loads(response)
    return response
    
def delete_one_contact(api_key, contact_id):
    """
    A function to delete contacts from a phonebook using the termii API

    Params:
    api_key: str
        The API key for a certain termii account
    contact_id: str
        The id of the contact to be deleted
    """

    response = requests.delete(url=f"{DELETE_CONTACT_URL}/{contact_id}?api_key={api_key}")
    response = json.loads(response)
    return response
