import threading
import time
from datetime import datetime, timedelta
from enum import Enum

class TimeFormat(Enum):
    HOUR_12 = 1
    HOUR_24 = 2

class Alarm:
    def __init__(self, alarm_time: datetime, label: str = "Alarm"):
        self.alarm_time = alarm_time
        self.label = label

    def is_due(self, current_time: datetime) -> bool:
        return current_time.strftime('%H:%M:%S') == self.alarm_time.strftime('%H:%M:%S')
    
class DigitalClock():
    def __init__(self, timeFormat = TimeFormat.HOUR_12):
        self.current_time = datetime.now()
        self.timeFormat = timeFormat
        self.alarms = []
        self.running = False

    def tick(self):
        self.current_time += timedelta(seconds=1)
    def change_format(self, timeFormat):
        self.timeFormat = timeFormat

    def display_time(self):
        if self.timeFormat == TimeFormat.HOUR_24:
            return self.current_time.strftime("%H:%M:%S")
        else:
            return self.current_time.strftime("%I:%M:%S %p")
        
    def set_alarm(self, alarm_time: datetime, label: str = "Alarm"):
        self.alarms.append(Alarm(alarm_time, label))

    def remove_alarm(self, label: str):
        self.alarms = [alarm for alarm in self.alarms if alarm.label != label]

    def check_alarms(self):
        for alarm in self.alarms:
            if alarm.is_due(self.current_time):
                print(f"🔔 {alarm.label} ringing at {self.display_time()}!")

    def run_clock(self):
        self.running = True
        while self.running:
            print(self.display_time())
            self.check_alarms()
            time.sleep(1)

    def stop_clock(self):
        self.running = False

clock = DigitalClock()
print(clock.display_time()) 
clock.tick()
print(clock.display_time()) 
alarm_time = clock.current_time + timedelta(seconds=3)
clock.set_alarm(alarm_time, "Wake up")

clock_thread = threading.Thread(target=clock.run_clock)
clock_thread.start()

# To stop after some time (optional demo):
time.sleep(10)
clock.stop_clock()