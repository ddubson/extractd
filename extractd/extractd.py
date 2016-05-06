import sys
import paramiko
import signal
from server import Server
from arg_reader import ArgReader
import socket

ssh = paramiko.SSHClient()


def repl(ssh, host):
    while True:
        com = raw_input(host + " $> ")
        if com == 'quit':
            signal_handler('', '')

        stdin, stdout, stderr = ssh.exec_command(com)

        if com == 'hostname':
            print stdout.read()
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
    except socket.error, e:
        print "Could not connect to server"
        sys.exit(1)

    print "Connected."
    repl(ssh, server.host)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main(sys.argv[1:])
