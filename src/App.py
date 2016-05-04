import sys
import getopt
import paramiko


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

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, password=password)
    stdin, stdout, stderr = ssh.exec_command("uptime")
    print stdout.readlines()


if __name__ == "__main__":
    main(sys.argv[1:])
