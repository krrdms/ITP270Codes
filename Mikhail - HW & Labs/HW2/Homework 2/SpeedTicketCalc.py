import json
from datetime import datetime
import uuid  # Outputs something like: UUID('0172fc9a-1dac-4414-b88d-6b9a6feb91ea')


def randomString(string_length=5):
    random = str(uuid.uuid4())  # This converts the UUID format into a string
    random = random.upper()  # Make all characters uppercase
    random = random.replace("-", "")  # removes uuid '-'
    return random[0:string_length]  # returns the string


def speedingTicket():
    speedLimit = int(input("\033[1mEnter speed limit:\033[0m "))
    actualSpeed = int(input("\033[1Enter actual speed:\033[0m "))
    ticketBase = 20
    ticketFine = (actualSpeed - speedLimit) * 5
    spa = (ticketBase // 10) * 10  # State Penalty Assessment
    scfa = (ticketBase // 10) * 5  # State Court Fund Assessment
    totalFine = ticketBase + ticketFine + spa + scfa  # Fine total
    if actualSpeed <= speedLimit:
        return
    else:
        print("\033[1m\033[4mSpeed Limit:\033[0m " + str(speedLimit))
        print("\033[1m\033[4mActual Speed:\033[0m " + str(actualSpeed))
        print("\033[1m\033[4mTotal Fine:\033[0m " + '$' + str(totalFine))

        # Data to be written
        caseNum = randomString()
        dataArray = [];
        speedTicket = {
            # "Case Reference": caseNum,
            "Date": str(datetime.now().strftime('%b-%d-%Y')),
            "Time": str(datetime.now().strftime('%X')),
            "Speed Limit": str(speedLimit),
            "Actual Speed": str(actualSpeed),
            "Fine": '$' + str(totalFine),
        }
        dataArray = speedTicket;
        # Serializing json
        with open("SpeedingTickets.json", "a") as outfile:
            outfile.write(json.dumps(dataArray, separators=(',', ':'), indent=4))
            outfile.write('\n' '')
            outfile.write(randomString())


speedingTicket()

# --------------------------------------------------------------------
# This was to test outputting to a txt file  (This also works)
#
# def speedingT1cket():
#    speed_limit = int(input("Speed Limit: "))
#    actual_speed = int(input("Actual Speed: "))
#    base = 20
#    fine = (actual_speed - speed_limit) * 5
#    spa = (base // 10) * 10  # State Penalty assessment
#    scfa = (base // 10) * 5  # State Court Fund assessment
#    total_fine = base + fine + spa + scfa
#    print(total_fine)
#    stFile = open("SpeedingFines.txt", "a")  # opening a file in append mode
#    stFile.writelines("Speed Limit: {}, Actual Speed: {}   Fine: ${}\n".format(speed_limit, actual_speed, total_fine))
#    stFile.close()  # always close the file once you are done using it.
#
#
# speedingT1cket()
