from datetime import datetime
import time
import winsound


class AlarmClock:
    def __init__(self , time_string):
        time_object = datetime.now()
        self.time = time_object.strftime('%H:%M:%S')
        self .alarm = time.strptime( time_string, '%H:%M:%S')

    def sound_alarm(self):
        set_alarm = self.alarm
        hour = set_alarm[3]
        minute = set_alarm[4]
        second = set_alarm[5]

        hour_str = f"{ hour:02d}"
        minute_str = f"{minute:02d}"
        second_str = f"{second:02d}"
        time_str = f'{hour_str}:{minute_str}:{second_str}'

        print(hour_str, minute_str, second_str)
        print(self.time)
        var= self.time

        if time_str == self.time:
            print("WAke Up")
            frequency = 2500
            duration =10000
            winsound.Beep(frequency, duration)
       
time_string= input("Enter the time for alarm: %H:%M:%S")

while True:
    alarm = AlarmClock(time_string)
    print(alarm.time, end="")
    AlarmClock.sound_alarm(alarm)
    time.sleep(1)
    print(end='\r')


