class Branch:
    def __init__(self, branch_number: int, branch_name: str, branch_suburb: str, branch_phonenumber: int) -> None:
        self.__b_number = branch_number
        self.__b_name = branch_name
        self.__b_suburb = branch_suburb
        self.__b_phoneno = branch_phonenumber
        self.b_status = "Closed"

    def open_branch(self):
        if self.b_status == "Closed":
            self.b_status = "Opened"
            print(f"{self.__b_name} is now {self.b_status}")
        else:
            print(f"{self.__b_name} is {self.b_status}, therefore it cannot be Opened")

    def closed_branch(self):
        if self.b_status == "Opened":
            self.b_status = "Closed"
            print(f"{self.__b_name} is now {self.b_status}")
        else:
            print(f"{self.__b_name} is {self.b_status}, therefore it cannot be Closed")

    def set_upd_branch_no(self, new_number: int):
        if isinstance(new_number, int) and len(str(new_number)) == 9:
            self.__b_phoneno = new_number
            print(f"The Branch phone number is changed to: {self.__b_phoneno}")
        else:
            print(f"Please enter a valid 9 digit phone number starting after 0")

    def feedback(self, branch_feedback: str):
        print(f"Feedback: {branch_feedback}")

    def __str__(self):
        print(f"The branch number is {self.__b_number}, and its name is {self.__b_name}. Its located in {self.__b_suburb}")
        print(f"its phone number is {self.__b_phoneno} and its current status is {self.b_status}")

    def set_change_branch_name(self, new_branch_name: str):
        if isinstance(new_branch_name, str):
            self.__b_name = new_branch_name
            return f"branch name has been changed to {self.__b_name}"
        else:
            print("please enter branch name again, it can only have letters")
    
    def set_change_branch_suburb(self, new_suburb: str):
        if isinstance(new_suburb, str):
            self.__b_suburb = new_suburb
            return f"branch {self.__b_number} suburb has been changed to {self.__b_suburb}"
        else:
            print("Please enter the address again, it has to be in string")
    


    def __repr__(self):
        print(f"Branch Number: {self.__b_number}\n\
              Name: {self.__b_name}\n\
              Location: {self.__b_suburb}\n\
              Phone number: {self.__b_phoneno}\n\
              Current Status: {self.b_status}")
    


    
