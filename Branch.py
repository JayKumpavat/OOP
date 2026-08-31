class Branch:
    def __init__(self, branch_number: str, branch_name: str, branch_suburb: str, branch_phonenumber) -> None:
        self.b_number = branch_number
        self.b_name = branch_name
        self.b_suburb = branch_suburb
        self.b_phoneno = branch_phonenumber
        self.b_status = "Closed"

    def open_branch(self):
        if self.b_status == "Closed":
            self.b_status = "Opened"
            return f"Branch is now {self.b_status}"
        else:
            return f"Branch is {self.b_status}, therefore it cannot be Opened"

    def closed_branch(self):
        if self.b_status == "Opened":
            self.b_status = "Closed"
            return f"Branch is now {self.b_status}"
        else:
            return f"Branch is {self.b_status}, therefore it cannot be Closed"

    def upd_branch_no(self, new_number: int):
        if len(str(new_number)) == 9:
            self.b_phoneno = new_number
            return f"The Branch phone number is changed to: {self.b_phoneno}"
        else:
            return f"Please enter a valid 10 digit phone number"

    def feedback(self, branch_feedback: str):
        print(f"Feedback: {branch_feedback}")

    
