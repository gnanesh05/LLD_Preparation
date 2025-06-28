from datetime import datetime, timedelta
from enum import Enum
import time
import threading
'''
Please implement an alarm clock using Object Oriented Programming. The alarm clock should have the following features:
 
• It displays the current time

• A user can create any number of alarms by specifying the alarm time and days of the week

and time when the alarm should alert. The alarm rings every 5 minutes, maximum of 3 times.

• User can snooze the alarm

• A user can delete an alarm
 
As a litmus test, using the data types created, create an alarm for 7 a.m. Mon - Fri and show how to go about snooze
 
https://github.com/jalantechnologies/flask-react-template
GitHub - jalantechnologies/flask-react-template: Boilerplate code for building projects using Python, Flask and React
Boilerplate code for building projects using Python, Flask and React - jalantechnologies/flask-react-template
 
'''

# we need Clock - for displaying current time | Alarm - set/snooze/cancel 

class Clock:
    def get_current_time(self):
        return datetime.now()
    
    def display_time(self):
        now = self.get_current_time()
        print("Current time:", now.strftime("%I:%M:%S %p"))

    
class Alarm:
    def __init__(self, time:str, days:list[str]):
        self.alarm_time = time
        self.days = days
        self.ring_count = 0
        self.max_ring = 3
        self.snoozed_until = None

    def should_ring(self,now:datetime):
        day = now.strftime("%A")
        time_match = now.strftime("%H:%M") ==  self.alarm_time
        snoozed = self.snoozed_until and  now < self.snoozed_until
        return day in self.days and time_match and not snoozed and self.ring_count < self.max_ring
    
    def ring(self):
        self.ring_count +=1
        print(f"Alarm ringing for {self.alarm_time} attempt - {self.ring_count} / {self.max_ring}")

    def snooze(self):
        self.snoozed_until = datetime.now() + timedelta(minutes=5)
        print(f"Snoozing alarm until {self.snoozed_until} attempt - {self.ring_count} / {self.max_ring}")


    def reset(self):
        self.ring_count = 0
        self.snoozed_until = None


class AlarmManager:
    def __init__(self):
        self.alarms: list[Alarm] = []

    def add_alarm(self, alarm):
        self.alarms.append(alarm)

    def remove_alarm(self, alarm):
        self.alarms.remove(alarm)

    def get_Active_alarms(self):
        return self.alarms
    

class AlarmNotifier:
    def __init__(self, clock:Clock, manager:AlarmManager):
        self.clock = clock
        self.manager = manager
        self.running = False


    def start(self):
        self.running = True
        def run():
            while self.running:
                now = self.clock.get_current_time()
                for alarm in self.manager.get_Active_alarms():
                    if alarm.should_ring(now):
                        alarm.ring()
                time.sleep(60)
        
        threading.Thread(target=run,daemon=True).start()


    def stop(self):
        self.running = False




clock = Clock()
manager = AlarmManager()

alarm1 = Alarm("22:26",["Friday"])
manager.add_alarm(alarm1)

notifier = AlarmNotifier(clock, manager)

notifier.start()                

time.sleep(5)
alarm1.snooze()

time.sleep(10)
notifier.stop()

    
    