from message import Message
from interface import UserInterface

def accounts(amount):
    print([1,2,3,4,5,6, amount])

def main():
    message = Message()
    ui = UserInterface()

    ui.register_command("/account", accounts, "shows a list of all accounts")
    

    ui.show_commands()
    ui.execute_command('/test', amount="seventy sever")

    message.print("Welcome to the bank of Py")
    while True:
        message.print("What can we do for you today?")
        user_input = input().lower()

        #exit check
        if(user_input == "exit"):
            print("Good bye")
            break

        message.print(user_input)



if __name__ == "__main__":
    main()