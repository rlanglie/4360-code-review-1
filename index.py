from message import Message
from interface import UserInterface
from user import User
from account import Account
from auth import Auth

def main():
    message = Message()
    ui = UserInterface()
    auth = Auth()
    
    #authenticate user
    login_attempts = 0
    failedAttempt = False
    while login_attempts < 3:

        ui.clear_screen()

        if failedAttempt:
            message.print("please try again")
        message.print("Welcome to the bank of Py!")
        message.print("please login to continue.")

        username = input("Username: ") #4 userName -> username
        password = input("Password: ") #2 made text consistent

        user = auth.login(username, password)
        if not user:
            login_attempts += 1
            failedAttempt = True
        else:
            break

    #register UI
    ui.register_command("deposit", user.deposit, "deposit [accountNumber] [amount] - deposit an amount into an account")
    ui.register_command("withdraw", user.withdraw, "withdraw [accountNumber] [amount] - withdraw an amount from an account")
    ui.register_command("transfer", user.transfer, "transfer [fromAccountNumber] [toAccountNumber] [amount] - transfer an amount from one account to another account") #6 removed a space :)

    #Main Loop
    while True:
        ui.clear_screen()
        message.print("What can we do for you today?")
        user.show_accounts()
        ui.show_commands()
        user_inputs = input().lower().split(" ")

        #exit check
        if(user_inputs[0] == "exit"):
            ui.clear_screen()
            print("Good bye")
            break

        
        ui.execute_command(user_inputs[0], user_inputs[1:])
        



if __name__ == "__main__":
    main()
   

