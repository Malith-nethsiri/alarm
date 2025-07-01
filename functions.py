# functions

import datetime
import time



# This is an alarm clock program
def set_alarm(alarm_time):
    print("Alarm set for:", alarm_time)
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Alarm ringing! Current time is:", current_time,"\nTime to wake up!\n")
            break

        elif current_time > alarm_time:
            print("Alarm time has passed. Current time is:",current_time ,"\n")
            break
        time.sleep(1)



# This is a stopwatch program

def format_time(elapsed_time):
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    miliseconds = int((elapsed_time % 1) * 1000)

    return f"{hours:02}:{minutes:02}:{seconds:02}.{miliseconds:03d}"

def stopwatch():
    print("Stopwatch started. Press Ctrl+C to stop.")
    start_time = time.time()
    try:
        while True:
            elapsed_time = time.time()- start_time
            formated =format_time(elapsed_time)
            print(f"\rElapsed time: {formated}", end="\r")
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("\nStopwatch stopped.\n")
