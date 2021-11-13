def calcPay(payRate, hours):
    # convert to int
    payRate = int(payRate)
    hours = int(hours)

    # Hour check
    if (hours > 80):
        extraHour = hours % 80
        totalPay = (payRate * 80) + (1.5 * payRate * extraHour)
    else:  # no extra hours worked
        totalPay = (payRate * hours)
    return totalPay


def getEmpl():
    empls = []
    n = int(input("\033[1mEnter number of employees:\033[0m "))

    for i in range(n):
        e = []
        # Get imputs
        name = input("\n\033[1mEnter name:\033[0m ")
        payRate = input("\033[1mEnter pay rate:\033[0m ")
        hours = input("\033[1mEnter hours worked:\033[0m ")

        e.append(name)
        e.append(payRate)
        e.append(hours)

        totalPay = calcPay(payRate, hours)  # Call function
        e.append(totalPay)

        empls.append(e)

    # output display
    for each in empls:
        print(f"\033[1m\n-----------------\n\033[4mCalculation Pay\033[0m\033[0m")
        print(f"\033[1mName:\033[0m \033[4m{each[0]}\033[0m\n\033[1mPay Rate:\033[0m \033[4m${each[1]}\033[0m\n\033[1mHours Worked:\033[0m \033[4m{each[2]}\033[0m\n\033[1mTotal Pay:\033[0m \033[4m${each[3]}\033[0m")
        print(f"\033[1m-----------------\033[0m")


getEmpl()
