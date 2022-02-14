from pydoc import cli
from client import Client

Phonebook_id = "5f74a4b2-84f9-446a-99ab-be902b6c932c"

client = Client("TLP5Z7WVApOTkOtnRckecOGiOyNzY61x8A3LwIdwVNO8PAGhyrslhB6jKKxTHy")

response = client.fetch_history()
"""response = client.send_token(
    message_type = 'NUMERIC',
    phone_number = "2347038659855", 
    sender_id = 'Munche',
    channel = 'generic',
    pin_attempts = 2,
    pin_time_to_live = 5,
    pin_length = 4, 
    pin_placeholder = '< >',
    message_text = "Your pin is < >",
)"""
"""response = client.voice_token(
    phone_number = "2347038659855",
    pin_attempts = 2,
    pin_time_to_live = 5,
    pin_length = 5,
)"""
"""response = client.voice_call(
    phone_number = "2347038659855",
    code = 34567,
    pin_attempts = 2,
    pin_time_to_live = 5,
    pin_length = 5,
)"""
"""response = client.verify_token(
    pin_id = '5ad13744-d43d-4d24-9531-386976f5d589',
    pin = 34567,
)"""
response = client.in_app_token(
    phone_number = "2347038659855",
    pin_attempts = 3,
    pin_time_to_live = 10,
    pin_length = 6,
)
print(response)