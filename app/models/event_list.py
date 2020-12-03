import datetime
from event import *

event1 = Event(datetime.date(2021, 5, 8), "CLassic Car Meet", "150", "Car Park", "This is car meet")
event2 = Event(datetime.date(2020, 12, 25), "Christmas Crazy-Fun-Time", "1", "My House", "No-one is invited")
events = [event1, event2]

def add_new_event(event):
    events.append(event)