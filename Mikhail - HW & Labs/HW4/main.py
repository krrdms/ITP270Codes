from Employee import Employee

employees = []

with open("EmplData.txt", "r") as f:
    lines = f.readlines()
    for data in lines:
        data = data.strip()
        employeeSep = data.split(",")
        employees.append([employeeSep[2], Employee(
            employeeSep[0], employeeSep[1], float(employeeSep[3]), int(employeeSep[4]))])
    f.close()

print("=======EMPLOYEES=======")
with open("EmployeeObjects.txt", "w") as f:
    for each in employees:
        f.write(each[0] + " " + each[1].getLastName() + ' ' + each[1].getFirstName() + " " + str(each[1].calcWeeklySalary()) + "\n")
        print(each[0] + " " + each[1].getLastName() + ' ' + each[1].getFirstName() + " " + str(each[1].calcWeeklySalary()))
    f.close()

print("=======SALARIES OVER 2600=======")
result = filter(lambda x: x[1].calcWeeklySalary() > 2600, employees)
for each in result:
    print('\n' + each[0] + " " + each[1].getLastName() + " " + each[1].getFirstName() + " " + str(each[1].calcWeeklySalary()))
