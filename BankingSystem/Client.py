class Client:
    def __init__(
        self,
        client_name,
        client_id,
        client_no,
    ):
        self.client_name = client_name
        self.__client_id = client_id
        self.__client_no = client_no

    def display_client_info(self):
        print("Client ID:", self.__client_id)
        print("Client Name:", self.client_name)
        print("Client Number:", self.__client_no)

    def set_change_client_number(self, new_number):
        self.__client_no = new_number
        print("Client number updated to:", self.__client_no)

    def set_client_name(self, new_name):
        self.client_name = new_name
        return f"Name has been changed to {self.client_name}"


    def __str__(self):
        print(f"Client's Id is {self.__client_id} and client name is {self.client_name} and their phone number is {self.__client_no}")

    def __repr__(self):
        print(f"Client Id: {self.__client_id}\n\
            Client Name: {self.client_name}\n\
            Client Phone Number: {self.__client_no}")




