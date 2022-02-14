from client import Client

Phonebook_id = "5f74a4b2-84f9-446a-99ab-be902b6c932c"

client = Client("TLP5Z7WVApOTkOtnRckecOGiOyNzY61x8A3LwIdwVNO8PAGhyrslhB6jKKxTHy")

response = client.add_contacts(r'C:\Users\Panam\Documents\termii-python\termii\contacts.csv', '234', 'text/csv', Phonebook_id)
print(response)