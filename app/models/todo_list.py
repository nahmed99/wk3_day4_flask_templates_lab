from app.models.event import *


event1 = Event('2020-12-01', "The gathering", 25, 'Glasgow City', "Lot's of people gathering in one location")
event2 = Event('2020-12-05', "The walk", 13, 'West Central Scotland', "Some people out for a walk")
events = [event1, event2]


# the following function is not used...
# def add_new_task(event):
#     events.append(event)
