from lib import status

def check(name):
    i = 0

    while i < len(name):
        if name[i] == ' ':
            print("\n%s Username can't be made of space" % status.error())
            return (-1)
        if name[i] == '/':
            print("\n%s Username can't be made of slashe" % status.error())
            return (-1)
        if name[i] == '\\':
            print("\n%s Username can't be made of back-slashe" % status.error())
            return (-1)
        i += 1
    return (0)