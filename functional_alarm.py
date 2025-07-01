# this is a alarm clock program

import datetime
from functions import set_alarm, stopwatch

running = True

while running:

    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print("Current time is:", current_time)

    programm = input("Press 'a' to set an alarm, 's' to start a stopwatch, or 'x' to exit: ").strip().lower()

    if programm == "a":
        try:
            alarm = input("Set alarm time in HH:MM format ")

            if len(alarm) == 5 and alarm[2] == ':':
                alarm_time = datetime.datetime.strptime(alarm, "%H:%M").strftime("%H:%M:%S")
                set_alarm(alarm_time)

            else:
                print("Invalid time format. Please use HH:MM format.\n")

        except ValueError:
            print("Invalid input. Please enter a valid time in HH:MM format.\n")

    elif programm == "s":
        stopwatch()


    elif programm == "x":
        print("Exiting the alarm clock program.")
        running = False
