class Branch:
    def __init__(
        self,
        branch_number: int,
        branch_name: str,
        branch_suburb: str,
        branch_phonenumber: int,
    ) -> None:

        if isinstance(branch_number, int):
            self.__b_number = branch_number
        if isinstance(branch_name, str):
            self.__b_name = branch_name
        if isinstance(branch_suburb, str):
            self.__b_suburb = branch_suburb
        if isinstance(branch_phonenumber, int):
            self.__b_phoneno = branch_phonenumber
        self.__b_status = "Closed"

    # open and closing branch while checking if they are already closed/ open. 
    def open_branch(self):
        if self.__b_status == "Closed":
            self.__b_status = "Opened"
            print(f"{self.__b_name} is now {self.__b_status}")
        else:
            print(f"{self.__b_name} is {self.__b_status}, therefore it cannot be Opened")

    def closed_branch(self):
        if self.__b_status == "Opened":
            self.__b_status = "Closed"
            print(f"{self.__b_name} is now {self.__b_status}")
        else:
            print(f"{self.__b_name} is {self.__b_status}, therefore it cannot be Closed")

    # updating branch phonenumber
    def set_upd_branch_no(self, new_number: int):
        if isinstance(new_number, int) and len(str(new_number)) == 9:
            self.__b_phoneno = new_number
            print(f"The Branch phone number is changed to: {self.__b_phoneno}")
        else:
            print(f"Please enter a valid 9 digit phone number starting after 0")

    # if customers want to give feedback to branch
    def feedback(self, branch_feedback: str):
        print(f"Feedback: {branch_feedback}")

    # changing branch name and suburb (for admin only)
    def set_change_branch_name(self, new_branch_name: str):
        if isinstance(new_branch_name, str):
            self.__b_name = new_branch_name
            return f"branch name has been changed to {self.__b_name}"
        else:
            print("please enter branch name again, it can only have letters")

    def set_change_branch_suburb(self, new_suburb: str):
        if isinstance(new_suburb, str):
            self.__b_suburb = new_suburb
            return (
                f"branch {self.__b_number} suburb has been changed to {self.__b_suburb}"
            )
        else:
            print("Please enter the address again, it has to be in string")

    # __str__
    def __str__(self):
        print(
            f"The branch number is {self.__b_number}, and its name is {self.__b_name}. Its located in {self.__b_suburb}"
        )
        print(
            f"its phone number is {self.__b_phoneno} and its current status is {self.__b_status}"
        )

    # __repr__
    def __repr__(self):
        print(f"Branch Number: {self.__b_number}\n\
              Name: {self.__b_name}\n\
              Location: {self.__b_suburb}\n\
              Phone number: {self.__b_phoneno}\n\
              Current Status: {self.__b_status}")

# testing purpose only
#   def get_branch_name(self):
#        return self.__b_name
    