from datetime import datetime, timedelta
from schedules import watch_schedule, bell_schedule
import copy

class Time:
    def __init__(self, time='00:00'):
        hour, minute = time.split(':')
        self.hour = int(hour)
        self.minute = int(minute)
        self.time_str = time

    def __sub__(self, other):
        temp = copy.copy(self)
        if other.hour == 23 and self.hour == 0:
            temp.hour = 24

        hours = temp.hour - other.hour
        minutes = temp.minute - other.minute
        return hours * 60 + minutes

    def __lt__(self, other):

        temp = copy.copy(other)
        if self.hour >= 20 and other.hour == 0:
            temp.hour = 24

        if (self - temp) < 0:
            return True
        else:
            return False
        
    def __le__(self, other):
        temp = copy.copy(other)
        if self.hour >= 20 and other.hour == 0:
            temp.hour = 24

        if (self - other) < 0 or (self - other) == 0:
            return True
        else:
            return False

    def now(self):
        n = datetime.now()
        self.hour = n.hour
        self.minute = n.minute
        return self

class Watch():
    def __init__(self, name, start, end):
        self.name = name
        self.start = Time(start)
        self.end = Time(end)

class Bell(Time):
    def __init__(self, time, count):
        self.time = Time(time)
        self.count = count

class Schedule:
    def __init__(self, now=Time().now()):

        if isinstance(now, str):
            self.now = Time(now)
        elif isinstance(now, Time):
            self.now = now

        self.watches = []
        for watch in watch_schedule:
            self.watches.append(Watch(watch['name'], watch['start'], watch['end']))

        self.bells = []
        for bell in bell_schedule:
            self.bells.append(Bell(bell['time'], bell['count']))

    def current_watch(self):
        for watch in self.watches:
            if watch.start <= self.now < watch.end:
                return watch

    def next_watch(self):
        for i, watch in enumerate(self.watches):
            if watch.start <= self.now < watch.end:
                if i+1 <= len(self.watches)-1:
                    return self.watches[i+1]
                else:
                    return self.watches[
                        i+1 - len(self.watches)
                    ]

    def last_watch(self):
        for i, watch in enumerate(self.watches):
            if watch.start <= self.now < watch.end:
                return self.watches[i-1]

    def next_bell(self):
        prev_bell = self.bells[-1]
        for bell in self.bells:
            if prev_bell.time <= self.now < bell.time:
                return bell
            prev_bell = bell

    def last_bell(self):
        prev_bell = self.bells[-1]
        for i, bell in enumerate(self.bells):
            if prev_bell.time <= self.now < bell.time:
                return self.bells[i-1]
            prev_bell = bell

    def min_to_next_bell(self):
        return self.next_bell().time - self.now
    
    def min_since_last_bell(self):
        return self.now - self.last_bell().time

if __name__ == '__main__':

    # This program converts any time of day into Ship's Bell Time!
    # Ship's Bell Time is a system of time-keeping that has been used aboard marine vessels since as early
    # as the 1400s and is still in-use today! This system divides the day (24hrs) into 7 "watches". 
    #
    # WATCH         START    END
    # ----------------------------
    # First         20:00    00:00
    # Middle        00:00    04:00
    # Morning       04:00    08:00
    # Forenoon      08:00    12:00
    # Afternoon     12:00    16:00
    # First Dog     16:00    18:00
    # Second Dog    18:00    20:00
    #
    # The progress of each watch is announced every 30 minutes by ringing the ship bell. 
    # For example, consider a 4 hour watch. After the first 30 minutes, the bell is rung once 
    # for "First Bell". After the next 30 minutes the bell is rung twice for "Two Bells". 
    # After 30 more minutes it's rung thrice "Three Bells", and so on. After all 4 hours have passed
    # (8 30min increments) the bell is rung for "Eight Bells" indicating the end of the 
    # current watch and the beginning of the next. 
    # Enough explaination, here's how to use this program to check the watch status for a given time!

    # Start by initializeing the Scheudle with the target time.
    s = Schedule('20:11') # Pass the target time as a string like (ie. '23:45', '00:28', '15:13', etc.)
    s = Schedule()        # ...or leave it blank and it'll default to current time!

    # Use the Schedule you created to check the watch status for the time...
    current_watch = s.current_watch().name
    next_watch = s.next_watch().name
    last_watch = s.last_watch().name

    # ...or status of the bell!
    next_bell = s.next_bell().count
    last_bell = s.last_bell().count
    minutes_to_next_bell = s.min_to_next_bell()
    minutes_since_last_bell = s.min_since_last_bell()

    # Example: Print out current time in human readable text.
    if minutes_to_next_bell == 1:
        units = 'minute'
    else:
        units = 'minutes'

    if next_bell == 1:
        next_bell_formated = 'First bell'
    else:
        next_bell_formated = f'{next_bell} bells'

    print(f"It's currently {current_watch} watch. {minutes_to_next_bell} {units} to {next_bell_formated}.")
