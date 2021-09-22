# no arguments
def ex1():
    pass

#both arguments required
def required_args(a,b):
    return a*b

#second argument is optional
def default_args(a,b=3):
    return a*b

#can take 0-n arguments - args kept in a list
def variable_args(*args):
    print("found %d args" % len(args))
    return sum(args)


def main():
    print ("default_args(5,5) [%d] vs default_args(5) %d" %
           (default_args(5,5), default_args(5)))
    print ("variable args sum (1-11 odds) %d" % variable_args(1,3,5,7,9,11))
    print ("variable args sum (10,20,30 odds) %d" % variable_args(10,20,30))


if __name__ == "__main__":
    # execute only if run as a script
    main()