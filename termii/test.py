from client import Client

Phonebook_id = "5f74a4b2-84f9-446a-99ab-be902b6c932c"

client = Client("TLP5Z7WVApOTkOtnRckecOGiOyNzY61x8A3LwIdwVNO8PAGhyrslhB6jKKxTHy")
options = {
    'email_address':'panampraisehebron@gmail.com',
    'first_name':'Hebron',
    'last_name':'Praise',
    'company':'Munche'
}
response = client.add_new_contact('2348056834458', Phonebook_id, '234', options)
print(response)