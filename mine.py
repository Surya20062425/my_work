def verify_pin(pin):
    pins = set()
    try:
        with open("pin.txt", 'r') as f:
            for line in f:
                pin = line.strip()
                if pin:  # Skip empty lines
                    pins.add(pin)
    except FileNotFoundError:
        print("File not found!")
        return False
    
    entered = input("Enter PIN: ").strip()
    if entered in pins:
        print("PIN verified! Access granted.")
        return True
    print("Invalid PIN.")
    return False

# Usage
verify_pin("pins.txt")
print("welcome to NO BANK")

balance=1000000

def withdrawl(amount):
    global balance
    if amount>balance:
        print("insufficient balance")
    else:
        balance-=amount
        print(f"withdrawl successful your remaining balance is :{balance}")
        
        
def deposit(amount):
    global balance
    balance+=amount
    print(f"deposit successful your new balance is :{balance}")
    
    
def check_balance():
    global balance
    print(f"your current balance is :{balance}")    
    
while True:
    print("1.withdrawl\n2.deposit\n3.check balance\n4.exit")
    choice=int(input("enter your choice:"))
    
    if choice==1:
        amount=int(input("enter the amount to withdrawl:"))
        withdrawl(amount)
        
    elif choice==2:
        amount=int(input("enter the amount to deposit:"))
        deposit(amount)
        
    elif choice==3:
        check_balance()
        
    elif choice==4:
        print("thank you for using NO BANK")
        break
        
    else:
        print("invalid choice please try again")