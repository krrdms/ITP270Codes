import json


# json_obj = '{"Name":"Programming for Cybersecurity","Code":"ITP","Number":"270"}'
#
# python_obj = json.loads(json_obj)
# print('\nJSON data:')
# print(python_obj)
# print('\nName: ', python_obj['Name'])
# print('Code: ', python_obj["Code"])
# print('Number: ', python_obj["Number"])
def fun(s):
    # this is the answer string
    answer = ""

    # it will split the string where it encounters a dash (-)
    # eg. '2004-01-23'.split() = ['2004','01','23']
    arr = s.split('-')

    # This retrieves value pair for the key arr[1] i.e. month
    # for this list ['2004','01','23'], it gives 01 .ie. january
    month = mon[arr[1]]
    ans = month + " " + arr[2] + ", " + arr[0]

    return ans


# this dictionary contains key value pair for months
mon = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
       '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}

# this dictionary will add the dates.
dictionary = {"American style": "International style"}

print("Please Enter 6 dates: ")
for i in range(6):
    a = input()
    american_date = fun(a)

    # adding the International and american_date
    dictionary[american_date] = a
    print(american_date)

print("The dictionary is : ", dictionary)

json_object = json.dumps(dictionary, indent=1)

# Writing to sample.json
with open("Dates.json", "a+") as outfile:
    outfile.write(json_object)
