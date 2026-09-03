# Portfolio

## **Week 1: Workshop 2**

Creating the two initial objects; Client and Account.
These two objects were created in a vscode file that was not linked to github so the changes and progress are not on the gitpage.
All code done before w2 workshop 1 (up to withdrawl and deposit) was done in that file and was transfered into this repo. 

### Overview of this weeks objective and the work that was completed

This week was an introductory week so workshop 1 did not have any tasks due. In workshop 2, the finance company senario was introduced and 
the task was to create two objects, client and account. The use of the __init__ constructor was used along with self. 

### Code for week 1: workshop 2:
class Client:
    def __init__(self, ClientName, ClientID, ClientNo):
        self.ClientName = ClientName
        self.ClientID = ClientID
        self.ClientNo = ClientNo

    def display_client_info(self):
        print("Client ID:", self.ClientID)
        print("Client Name:", self.ClientName)
        print("Client Number:", self.ClientNo)

    def change_client_Number(self, new_number):
        self.ClientNo = new_number
        print("Client number updated to:", self.ClientNo)

class Account:
    def __init__(self, AccNumber, AccType, Balance):
        self.AccNumber = AccNumber
        self.AccType = AccType
        self.Balance = Balance

    def Display_acc_info(self):
        print(f'Account No: {self.AccNumber}')
        print(f'Account Type: {self.AccType}')
        print(f'Account Balance: ${self.Balance}')

Client1 = Client("John Doe", "00001", "555-1234")
Client2 = Client("Toby Maguire", "00002", "555-1235")
Account1 = Account(1101, "Savings", 10000)
Account2 = Account(1102, "Savings", 500)


Account1.Transfering_ammount(Account2, 500)
Account2.Display_acc_info()
#Client1.display_client_info()
#Account1.Display_acc_info()
#Account1.Withdrawl(200)

### Testing outcomes:






### Comments on the code:




