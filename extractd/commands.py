__name__ = "commands"

extractd_dir = "~/.extractd"
cpu_file = extractd_dir + "/cpu.ex"
cpu_command = "rm -f {0} && echo -n \"Processor Family: \" >> {0} && \
        cat /proc/cpuinfo | grep 'model name' | cut -d':' -f2 >> {0} && \
        echo -n \"Physical CPU Count: \" >> {0} && \
        cat /proc/cpuinfo | grep 'physical id' | sort | uniq | wc -l >> {0} && \
        echo -n \"CPU Core Count: \" >> {0} && \
        cat /proc/cpuinfo | grep \"cpu cores\" | uniq | cut -d':' -f2 >> {0} && \
        cat {0}".format(cpu_file)

profiles = {
    "debian": {
        "os": "lsb_release -a"
    },
    "redhat": {
        "os": ""
    }
}

commandDictionary = {
    "cpu": cpu_command,
    "help": "help",
    "hostname": "hostname",
    "os": profiles.get("debian").get("os"),
    "quit": "quit"
}


def print_available_commands():
    print "Currently supported commands: "
    for k, v in commandDictionary.iteritems():
        print "- " + k
