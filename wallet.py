class Wallet:

    #Grab the initial balance in the account
    def __init__(self, initial_balance):
        self.balance = initial_balance

    #method that deposits funds to the balance
    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    #method that attempts to withdraw from the balance
    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
        else:
            print("Insufficient funds. You have " + str(self.balance) + " in your account. Please deposit more or withdraw less.")

    #display the balance
    def display_balance(self):
        print("The current balance in the account is " + str(self.balance))
        print("-----")

#Check if this module is the one currently being run
if __name__ == "__main__":
    #Ask user for initial balance
    initial_balance = int(input("Initial balance in account: "))
    #initiate the class, passing the initial balance
    wallet = Wallet(initial_balance)
    wallet.display_balance()
    while True:
        #Pick an option to withdraw, deposit or exit
        print("1: Deposit funds")
        print("2: Withdraw funds")
        print("3: Exit")
        type = int(input("Please select an option (1, 2 or 3): "))
        if type == 1:
            deposit_amount = int(input("Please specify amount to deposit: "))
            wallet.deposit(deposit_amount)
            wallet.display_balance()
        elif type == 2:
            withdraw_amount = int(input("Please specify amount to withdraw: "))
            wallet.withdraw(withdraw_amount)
            wallet.display_balance()
        elif type == 3:
            break
        else:
            print("Invalid selection, please type either 1, 2 or 3")
