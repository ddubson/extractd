import sys

import paramiko
import signal
from server import Server
from arg_reader import ArgReader
from commands import print_available_commands, commandDictionary, profiles
import socket

ssh = paramiko.SSHClient()


def repl(ssh, server):
    ssh.exec_command("mkdir -p ~/.extractd && chmod +w ~/.extractd")
    stdin, stdout, stderr = ssh.exec_command(profiles.get("debian").get("os"))
    print stdout.read()

    while True:
        com = raw_input("{0}@{1} $> ".format(server.username, server.host))
        if com == 'quit':
            signal_handler('', '')

        if com == 'help':
            print_available_commands()
            continue

        rawCom = commandDictionary.get(com)
        if rawCom is None:
            print "Command '{0}' is not a valid command.".format(com)
            continue

        stdin, stdout, stderr = ssh.exec_command(rawCom)

        if com == 'hostname':
            hostname = stdout.read()
            print "Hostname for this instance is: {0}".format(hostname)
        else:
            print stdout.read()


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
    print "------------------------------------"
    repl(ssh, server)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main(sys.argv[1:])
