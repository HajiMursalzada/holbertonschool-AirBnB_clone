import cmd

class HBNBCommand(cmd.Cmd):
    """ HBNBCommand Class """
    prompt = "(hbnb) "
    def do_EOF(self, line):
        """Exit Program"""
        return True
    def help_quit(self):
        """Help for quit"""
        print("Quit command to exit the program")
    def do_quit(self, line):
        """ Exit Program """
        return True
    def help_EOF(self):
        """Help for EOF"""
        print("EOF command to exit the program")
    def emptyline(self):
        """ Empty """
        return ""
if __name__ == '__main__':
    HBNBCommand().cmdloop()
