import datetime
import time
import winsound  # For Windows users, for other platforms, you might need a different library.

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            # You can customize the alarm sound or action here
            winsound.Beep(1000, 9000)  # Beep for 9 seconds
            
        time.sleep(1)

def main():
    print("Welcome to the Alarm Clock App")
    alarm_hour = input("Enter the hour (24-hour format): ")
    alarm_minute = input("Enter the minute: ")

    # Validate input
    try:
        alarm_time = datetime.time(int(alarm_hour), int(alarm_minute)).strftime("%H:%M:%S")
    except ValueError:
        print("Invalid input. Please enter valid numbers for the hour and minute.")
        return

    print(f"Alarm set for {alarm_time}")

    set_alarm(alarm_time) 

if __name__ == "__main__":
    main()



    



