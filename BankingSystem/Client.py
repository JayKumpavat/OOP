class Client:
    def __init__(
        self,
        client_name,
        client_id,
        client_no,
    ):
        self.client_name = client_name
        self.client_id = client_id
        self.client_no = client_no

    def display_client_info(self):
        print("Client ID:", self.client_id)
        print("Client Name:", self.client_name)
        print("Client Number:", self.client_no)

    def change_client_number(self, new_number):
        self.client_no = new_number
        print("Client number updated to:", self.client_no)

    def __str__(self):
        print(f"Client's Id is {self.client_id} and client name is {self.client_name} and their phone number is {self.client_no}")

    def __repr__(self):
        print(f"Client Id: {self.client_id}\n\
            Client Name: {self.client_name}\n\
            Client Phone Number: {self.client_no}")




