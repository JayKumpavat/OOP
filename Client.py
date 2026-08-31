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




