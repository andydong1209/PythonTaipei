from QuantLib import *
import pandas as pd

date = Date(31, 3, 2015)
print(date)

print("%d-%d-%d" %(date.month(), date.dayOfMonth(), date.year()))
date.weekday() == Tuesday

type(date+1)

print("Add a day : {0}".format(date + 1))
print("Subtract a day : {0}".format(date - 1))
print("Add a week : {0}".format(date + Period(1, Weeks)))
print("Add a month : {0}".format(date + Period(1, Months)))
print("Add a year : {0}".format(date + Period(1, Years)))

print(date == Date(31, 3, 2015))
print(date > Date(30, 3, 2015))
print(date < Date(1, 4, 2015))
print(date != Date(1, 4, 2015))

date = Date(31, 3, 2015)
us_calendar = UnitedStates()
italy_calendar = Italy()
period = Period(60, Days)
raw_date = date + period
us_date = us_calendar.advance(date, period)
italy_date = italy_calendar.advance(date, period)
print("Add 60 days: {0}".format(raw_date))
print("Add 60 business days in US: {0}".format(us_date))
print("Add 60 business days in Italy: {0}".format(italy_date))

us_busdays = us_calendar.businessDaysBetween(date, us_date)
italy_busdays = italy_calendar.businessDaysBetween(date, italy_date)
print("Business days US: {0}".format(us_busdays))
print("Business days Italy: {0}".format(italy_busdays))

joint_calendar = JointCalendar(us_calendar, italy_calendar)
joint_date = joint_calendar.advance(date, period)
joint_busdays = joint_calendar.businessDaysBetween(date, joint_date)
print("Add 60 business days in US-Italy: {0}".format(joint_date))
print("Business days US-Italy: {0}".format(joint_busdays))

