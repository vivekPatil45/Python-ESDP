

class SBIBank:
    def __init__(self):
        self.name_of_the_depositor = ""
        self.account_number = 0
        self.type_of_account = ""
        self.balance_account = 0.0
        self.addData()
    
    def addData(self):
        print("---------------SBI BANK----------------")
        self.name_of_the_depositor = input("Enter The Name of Depositor : ")
        self.account_number = int(input("Enter The Account Number : "))
        self.type_of_account = input("Enter The Type Of Account : ")
        self.balance_account = int(input("Enter The Account Balance : "))

    def deposite(self):
        print("---------------DEPOSITE MONEY----------------")
        bal = int(input("Enter The Amount To Deposite : "))
        self.balance_account += bal
        self.showData()
    
    def showData(self):
        print("---------------------------------------------------")
        print("Name of Account Holder = ",self.name_of_the_depositor)
        print("Account Number = ",self.account_number)
        print("Type Of Account = ",self.type_of_account)
        print("Account Balance = ",self.balance_account)
        

    
    def withdraw(self):
        print("---------------WITHDRAW MONEY----------------")
        bal = int(input("Enter The Amount To Withdraw :"))
        if(bal>500):
            self.balance_account -= bal
            self.showData()
        else:
            print("Not ENgough Money To withdraw")

        self.showData()
        
        

    def __del__(self):
        print("Destructor is called")
        




        



def main():
    s = SBIBank()
    while True:
        print("------------Bank Transcation-------------------")
        print("1.Deposite ")
        print("2.Withdraw ")
        print("3.Exit")
        print("-----------------------------------------------")
        ch = int(input("Enter Your Choice = "))
        print("-----------------------------------------------")
        if ch==1:
            s.deposite()
        elif ch==2:
            s.withdraw()
        elif ch==3:
            break
        else: 
            print("Enter The valid input")




if __name__=="__main__":
    main()



