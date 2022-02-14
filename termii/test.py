from client import Client

Phonebook_id = "5f74a4b2-84f9-446a-99ab-be902b6c932c"

client = Client("TLP5Z7WVApOTkOtnRckecOGiOyNzY61x8A3LwIdwVNO8PAGhyrslhB6jKKxTHy")

response = client.fetch_campaign_history('C620a709c7c512')
print(response)