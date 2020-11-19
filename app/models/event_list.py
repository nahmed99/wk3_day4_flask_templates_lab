from app.models.event import *


event1 = Event('2020-12-01', "The Gathering", 25, 'Glasgow City', "Lot's of people gathering in one location")
event2 = Event('2020-12-05', "The Walk", 13, 'West Central Scotland', "Some people out for a walk")
event3 = Event('2020-12-07', "The Big Talk", 5, 'Dundee', "Somebody giving an important talk about something that they care about")
event4 = Event('2020-12-09', "The Daily Yawn", 50, 'Webcast', "Democracy. Do people enjoy voting? Three-day conference")
event5 = Event('2020-12-12', "The Walk", 25, 'West Central Scotland', "Some more people out for a walk")

events = [event1, event2, event3, event4, event5]


# the following function is not used...
# def add_new_task(event):
#     events.append(event)
