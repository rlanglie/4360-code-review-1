'''
The UserInterface class holds a set of commands and their corresponding methods.
'''

from message import Message

class UserInterface:
    def __init__(self):
        self.commands = {}
        self.message = Message()

    def show_commands(self):
        for key,val in self.commands.items():
            message = key + " - " + val["description"]
            self.message.print(message)
            

    def register_command(self, command, callback, description=""):
        self.commands[command] = {
            "callback": callback,
            "description": description
        }

    def deregister_command(self, command):
        self.commands.pop(command)

    def execute_command(self, command, **kwargs):
        try:
            func = self.commands[command]["callback"]
            return func(**kwargs)
        except:
            self.message.print("sorry, that is not a valid command")