import termii_switch

class Client:
    """
    Creates a termi client using the api_key
    ...

    Attributes:
    api_key: str 
        The termii developer API Key to create a client from.
    """
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_sender_ids(self):
        """
        Simple function to request new termii sender ID.
        """
        response = termii_switch.get_sender_ids(self.api_key)
        return response
    
    def request_sender_id(self, sender_id, usecase, company):
        """
        Simple function to request new termii sender ID.

        Params:
        sender_id: str
            The name of the new sender_id to create
        usecase: str
            The usecase of the new sender_id. Must be at least 20 characters
        company: str
            The name of the company associated with this sender_id
        """

        response = termii_switch.request_new_sender_id(self.api_key, sender_id, usecase, company)
        return response
    
    def send_message(self, number_to, sender_id, message, message_type, channel, media_dict):
        """
        Function to send a message using the termii API.

        Params:
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
        response = termii_switch.post_message(self.api_key, number_to, sender_id, message, message_type, channel, media_dict)
        return response

    def send_bulk_sms(self, numbers_to, sender_id, message, message_type, channel):
        """
        Function to send bulk sms messages using the termii api.

        Params:
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

        response = termii_switch.post_message_bulk(self.api_key, numbers_to, sender_id, message, message_type, channel)
        return response

    def send_message_with_autogenerated_number(self, number_to, message):
        """
        Function to send messages to customers using Termii's auto-generated messaging numbers that adapt to customers location.

        Params:
        number_to: str
            The phone number the message should be sent to in international format. '+' should be excluded
        message: str
            The message to be sent.
        """

        response = termii_switch.number_message_send(self.api_key, number_to, message)
        return response

    def send_device_template(self, phone_number, device_id, template_id, data):
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

        response = termii_switch.template_setter(self.api_key, phone_number, device_id, template_id, data)
        return response

    def fetch_phonebooks(self):
        """
        A function to get all the phonebooks associated to a termii client
        """
        
        response = termii_switch.get_phonebooks(self.api_key)
        return response

    def create_phonebook(self, description, phonebook_name):
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
        response = termii_switch.make_phonebook(self.api_key, description, phonebook_name)
        return response
    
    def update_phonebook(self, phonebook_id, phonebook_name, phone_description):
        """
        Function to create a phonebook using the termii API

        Params:
        api_key: str
            The API key for a certain termii account
        phonebook_id: str
            The id of the phonebook to be updated
        phonebook_name: str
            The new name of the phonebook
        phonebook_description: str
            The new description of the phonebook
        """

        response = termii_switch.patch_phonebook(self.api_key, phonebook_id, phonebook_name, phone_description)
        return response

    def delete_phonebook(self, phonebook_id):
        """
        Function to delete a phonebook using the termii API

        Params:
        api_key: str
            The API key for a certain termii account
        phonebook_id: str
            The id of the phonebook to be updated
        """

        response = termii_switch.remove_phonebook(self.api_key, phonebook_id)
        return response
    
    def fetch_contacts(self, phonebook_id):
        """
        Function to get all the contacts associated to a termii phonebook

        Params:
        api_key: str
            The API key for a certain termii account
        phonebook_id: str
            The id of the phonebook
        """
        
        response = termii_switch.get_contacts_from_phonebook(self.api_key, phonebook_id)
        return response
    
    def add_new_contact(self, phone_number, phonebook_id, options):
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

        response = termii_switch.add_contact(self.api_key, phone_number, phonebook_id, options)
        return response
    
    def add_contacts(self, contact_file, country_code, extension, phonebook_id):
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

        response = termii_switch.add_many_contacts(self.api_key, contact_file, country_code, extension, phonebook_id)
        return response