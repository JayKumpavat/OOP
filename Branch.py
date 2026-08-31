class Branch:
    def __init__(self, branch_number, branch_name, branch_suburb, branch_phonenumber, branch_status = "closed") -> None:
        self.b_number = branch_number
        self.b_name = branch_name
        self.b_suburb = branch_suburb
        self.b_phoneno = branch_phonenumber
        self.b_status = branch_status

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

    