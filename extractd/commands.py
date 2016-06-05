__name__ = "commands"

extractd_dir = "~/.extractd"
cpu_file = extractd_dir + "/cpu.ex"

profiles = {
    "debian": {
        "os": "lsb_release -a"
    },
    "redhat": {
        "os": ""
    }
}

commandDictionary = {
    "cpu":
        "rm -f " + cpu_file + " && echo -n \"Processor Family: \" >> " + cpu_file + " && \
        cat /proc/cpuinfo | grep 'model name' | cut -d':' -f2 >> " + cpu_file + " && \
        echo -n \"Physical CPU Count: \" >> " + cpu_file + " && \
        cat /proc/cpuinfo | grep 'physical id' | sort | uniq | wc -l >> " + cpu_file + " && \
        echo -n \"CPU Core Count: \" >> " + cpu_file + " && \
        cat /proc/cpuinfo | grep \"cpu cores\" | uniq | cut -d':' -f2 >> " + cpu_file + " && \
        cat " + cpu_file,
    "help": "help",
    "hostname": "hostname",
    "os": profiles.get("debian").get("os"),
    "quit": "quit"
}


def print_available_commands():
    print "Currently supported commands: "
    for k, v in commandDictionary.iteritems():
        print "- " + k
