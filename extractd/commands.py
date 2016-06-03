__name__ = "commands"


commandDictionary = {
    "cpu": "cat /proc/cpuinfo | grep 'model name' | cut -d':' -f2",
    "help": "help",
    "hostname": "hostname",
    "quit": "quit"
}


def print_available_commands():
    print "Currently supported commands: "
    for k, v in commandDictionary.iteritems():
        print "- " + k
