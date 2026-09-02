class Branch:
    def __init__(self, branch_number: int, branch_name: str, branch_suburb: str, branch_phonenumber: int) -> None:
        self.b_number = branch_number
        self.b_name = branch_name
        self.b_suburb = branch_suburb
        self.b_phoneno = branch_phonenumber
        self.b_status = "Closed"

    def open_branch(self):
        if self.b_status == "Closed":
            self.b_status = "Opened"
            print(f"{self.b_name} is now {self.b_status}")
        else:
            print(f"{self.b_name} is {self.b_status}, therefore it cannot be Opened")

    def closed_branch(self):
        if self.b_status == "Opened":
            self.b_status = "Closed"
            print(f"{self.b_name} is now {self.b_status}")
        else:
            print(f"{self.b_name} is {self.b_status}, therefore it cannot be Closed")

    def upd_branch_no(self, new_number: int):
        if len(str(new_number)) == 9:
            self.b_phoneno = new_number
            print(f"The Branch phone number is changed to: {self.b_phoneno}")
        else:
            print(f"Please enter a valid 10 digit phone number")

    def feedback(self, branch_feedback: str):
        print(f"Feedback: {branch_feedback}")

    def __str__(self):
        print(f"The branch number is {self.b_number}, and its name is {self.b_name}. Its located in {self.b_suburb}")
        print(f"its phone number is {self.b_phoneno} and its current status is {self.b_status}")

    def __repr__(self):
        print(f"Branch Number: {self.b_number}\n\
              Name: {self.b_name}\n\
              Location: {self.b_suburb}\n\
              Phone number: {self.b_phoneno}\n\
              Current Status: {self.b_status}")
    


    
