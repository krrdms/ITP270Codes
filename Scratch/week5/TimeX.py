import time
import timeit
import random

# How to check how long code runs with timeit


def timeitSingle():
    # times how long one line of code takes

    print("timeit single:", timeit.timeit('output = 10*5'))


def timeitMultiExample():
    # generates series of random numbers the prints how long it took
    # by default repeats 5 times.
    import_module = "import random"
    testcode = ''' 
def test(): 
    return random.randint(10, 100)
'''
    print("timeit multi:", timeit.repeat(stmt=testcode, setup=import_module))


def timeExample():
    # use difference between two points of code
    startTime = time.time()
    thing = random.randint(10, 100)
    endTime = time.time()
    print("timeExample:", endTime - startTime)


def timeProcessExample():
    # calculate how long the whole process ran
    startTime = time.process_time()
    thing = random.randint(10, 100)
    endTime = time.process_time()
    print("timeProcessExample (usec):", endTime - startTime)


def main():
    timeitSingle()
    timeitMultiExample()
    timeExample()
    timeProcessExample()


if __name__ == "__main__":
    # execute only if run as a script
    main()
