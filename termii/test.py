from client import Client

Phonebook_id = "5f74a4b2-84f9-446a-99ab-be902b6c932c"

client = Client("TLP5Z7WVApOTkOtnRckecOGiOyNzY61x8A3LwIdwVNO8PAGhyrslhB6jKKxTHy")

response = client.fetch_history()
response = client.send_token(
    message_type = 'NUMERIC',
    phone_number = 2347038659855, 
    sender_id = 'SMITH',
    channel = 'generic',
    pin_attempts = 2,
    pin_time_to_live = 5,
    pin_length = 4, 
    pin_placeholder = '< >',
    message_text = "Your pin is < >",
)
print(response)