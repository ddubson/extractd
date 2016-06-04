import getopt
import sys


class ArgReader:
    def __init__(self):
        self._host = ''
        self._password = ''
        self._user = ''

    def read(self, argv):
        try:
            opts, args = getopt.getopt(argv, 'h:u:p:', ["host=", "user=", "password=", "help"])
        except getopt.GetoptError, e:
            print e
            sys.exit(2)

        for opt, arg in opts:
            if opt == "--help":
                print "Usage: extractd.py -h <host>"
            elif opt in ("-h", "--host"):
                self._host = arg
            elif opt in ("-u", "--user"):
                self._user = arg
            elif opt in ("-p", "--password"):
                self._password = arg

    @property
    def host(self):
        return self._host

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password
