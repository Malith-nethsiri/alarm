# this is a alarm clock program

import datetime
from math import e
from functions import set_alarm, stopwatch

running = True

while running:
    programm = input("Press 'a' to set an alarm, 's' to start a stopwatch, or 'x' to exit: ").strip().lower()

    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print("Current time is:", current_time)


    if programm == "a":
        try:
            alarm_time = input("Set alarm time in HH:MM format ")

            if len(alarm_time) == 5 and alarm_time[2] == ':':
                alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M").strftime("%H:%M:%S")
                set_alarm(alarm_time)

            else:
                print("Invalid time format. Please use HH:MM format.\n")

        except ValueError:
            print("Invalid input. Please enter a valid time in HH:MM format.\n")

    elif programm == "s":
        y_n = input("Do you want to start the stopwatch? (y/n): ").strip().lower()

        if y_n == 'y':
            stopwatch()

        elif y_n == 'n':
            print("Stopwatch not started.\n")
            continue

        else:
            print("Invalid input. Please enter 'y' or 'n'.\n")



    elif programm == "x":
        print("Exiting the alarm clock program.")
        running = False
