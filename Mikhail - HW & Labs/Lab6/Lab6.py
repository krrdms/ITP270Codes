class BankAccount:  # Default Pin: 1234

    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    # deposit function
    def deposit(self, pin, amt):
        if self.pin == pin:
            self.balance += amt
        # if pin is incorrect
        else:
            print("Incorrect pin")

    # withdraw function
    def withdraw(self, pin, amt):
        if self.pin == pin:
            # check if balance is sufficient
            if self.balance >= amt:
                self.balance -= amt
            else:
                print("Insufficient Balance")
        else:
            print("Incorrect pin")
            # get balance using this function

    def checkbal(self, pin):
        if self.pin == pin:
            return self.balance
        else:
            print("Incorrect pin")

    # change pin using this function
    def change_pin(self, pin, newPin):
        if self.pin == pin:
            self.pin = newPin
        else:
            print("Incorrect pin")


acc = BankAccount(1234, 0)
#  Menu
while True:
    print('''             ,d                        
             88                        
,adPPYYba, MM88MMM 88,dPYba,,adPYba,   
""     `Y8   88    88P'   "88"    "8a  
,adPPPPP88   88    88      88      88  
88,    ,88   88,   88      88      88  
`"8bbdP"Y8   "Y888 88      88      88 ''')
    print('╔═╦════════════════╗\n║1║ > Deposit      ║\n║2║ > Withdraw     ║\n║3║ > Check Balance║\n║4║ > Change Pin   ║\n'
          '║5║ > Exit         ║\n╚═╩════════════════╝')
    x = int(input('\nChoose an option: '))
    if x == 1:
        pin = int(input('\nPlease enter your pin: '))
        amt = float(input('Enter the amount to deposit: '))
        acc.deposit(pin, amt)
    elif x == 2:
        pin = int(input('\nPlease enter your pin: '))
        amt = int(input('Enter the amount to withdraw: '))
        acc.withdraw(pin, amt)
    elif x == 3:
        pin = int(input('\nPlease enter your pin: '))
        z = acc.checkbal(pin)
        if z is not None:
            print(f'\033[1m\nBalance:  ${z:,}')
    elif x == 4:
        pin = int(input('\nPlease enter your pin: '))
        newPin = int(input('Enter the pin you wish to use: '))
        acc.change_pin(pin, newPin)
        print('\nPin change successful\n')
    elif x == 5:
        break
    else:
        print('\033[1m\nIncorrect option, please try again\n')
