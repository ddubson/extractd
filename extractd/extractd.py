import sys
import paramiko
import signal
from server import Server
from arg_reader import ArgReader
from commands import print_available_commands, commandDictionary
import socket

ssh = paramiko.SSHClient()


def repl(ssh, server):
    while True:
        com = raw_input(server.username + "@" + server.host + " $> ")
        if com == 'quit':
            signal_handler('', '')

        if com == 'help':
            print_available_commands()
            continue

        stdin, stdout, stderr = ssh.exec_command(commandDictionary.get(com))

        if com == 'hostname':
            hostname = stdout.read()
            print "Hostname for this instance is: " + hostname
        elif com == 'cpu':
            cpuFam = stdout.read()
            print "Processor Model is " + cpuFam.strip()
        else:
            print stdout.readlines()


def signal_handler(signal, frame):
    ssh.close()
    print('\nExited successfully.')
    sys.exit(0)


def main(argv):
    args = ArgReader()
    args.read(argv)
    server = Server(args.host, args.user, args.password)
    try:
        print "Attempting to connect to " + server.host
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=server.host, username=server.username, password=server.password)
        print "..."
    except socket.error, e:
        print "Could not connect to server"
        sys.exit(1)

    print "Connected."
    print "-- Type 'quit' to disconnect."
    print "-- Type 'help' for list of commands."
    repl(ssh, server)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main(sys.argv[1:])
