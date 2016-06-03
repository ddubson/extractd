__name__ = "commands"


commands = {'cpu', 'help', 'hostname', 'quit'}


def print_available_commands():
    print "Currently supported commands: "
    for cmd in reversed(list(commands)):
        print "- " + cmd
