#Program Name: print_me_first
#Program Description:
#   This is a program to print student info, the lab name, and the current time
#
#   This program will output the name of the student, the lab name, and the time
#@Author : Zhenyu Jiang
#@Date: 09/30/2022
#

def printinfo():
    from datetime import datetime

    name = "CNET-142 - Zhenyu Jiang"
    print ("{:16}".format("Name"),":",name)
    Lab = "Lab 6 - Dictionary"
    print ("{:16}".format("Lab"),":",Lab)
    currentTime = datetime.now()
    time = currentTime.strftime("%b-%d-%Y %a (%I:%M:%S%p)")
    print("{:16}".format("Current Time"),":",time)
