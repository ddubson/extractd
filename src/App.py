import sys
import getopt
import paramiko
import signal

ssh = paramiko.SSHClient()

def repl(ssh):
    while True:
        com = raw_input("$> ")
        if com == 'quit':
            signal_handler('', '')

        stdin, stdout, stderr = ssh.exec_command(com)
        print stdout.readlines()


def signal_handler(signal, frame):
    ssh.close()
    print('\nExited successfully.')
    sys.exit(0)


def main(argv):
    host = ''
    user = ''
    password = ''

    try:
        opts, args = getopt.getopt(argv, 'h:u:p:', ["host=", "user=", "password=", "help"])
    except getopt.GetoptError, e:
        print 'host (-h) is required.'
        print e
        sys.exit(2)

    for opt, arg in opts:
        if opt == "--help":
            print "Usage: App.py -h <host>"
        elif opt in ("-h", "--host"):
            host = arg
        elif opt in ("-u", "--user"):
            user = arg
        elif opt in ("-p", "--password"):
            password = arg

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, password=password)
    repl(ssh)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main(sys.argv[1:])
