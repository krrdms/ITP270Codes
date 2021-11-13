def calcPay(payRate, hours):
    if hours > 80:
        overtime_hours = hours % 80
        totalPay = (payRate * 80) + (1.5 * payRate * overtime_hours)
    else:
        totalPay = (payRate * hours)
        return totalPay


def getEmpl():
    empls = []

    name = input("\033[1mEnter employee \033[4mname\033[0m\033[1m, or type '\033[4mx\033[0m\033[1m' to quit: \033[0m")

    while name != "x":
        payRate = int(input("\033[1mEnter pay \033[4mrate\033[0m: \033[0m"))
        hours = int(input("\033[1mEnter \033[4mhours\033[0m\033[1m worked: \033[0m"))
        record = (name, payRate, hours)
        empls.append(record)
        name = input("\033[1mEnter employee \033[4mname\033[0m\033[1m, or type '\033[4mx\033[0m\033[1m' to quit: "
                     "\033[0m")

        return empls


def main():
    emplDetails = getEmpl()

    for record in emplDetails:
        name, payRate, hours = record  # Retrieve these items from tuple
        totalPay = calcPay(payRate, hours)  # Calculating the total amount of pay
        print(f"\033[1m\n-----------------\n\033[4mCalculation Pay\033[0m\033[0m")
        print("Name:", name, "\nRate:", "$" + str(payRate) + "\nHours:", str(hours) + "\nTotal:", '$' + str(totalPay))
        print(f"\033[1m-----------------\033[0m")


main()
