# no arguments
def ex1():
    pass


def required_args(a,b):
    # both arguments required
    return a*b


def default_args(a,b=3):
    # second argument is optional
    return a*b


def variable_args(*args):
    # can take 0-n arguments - args kept in a list
    print("found %d args" % len(args))
    return sum(args)


def main():
    print("default_args(5,5) [%d] vs default_args(5) %d" %
           (default_args(5,5), default_args(5)))
    print("variable args sum (1-11 odds) %d" % variable_args(1,3,5,7,9,11))
    print("variable args sum (10,20,30 odds) %d" % variable_args(10,20,30))


if __name__ == "__main__":
    # execute only if run as a script
    main()