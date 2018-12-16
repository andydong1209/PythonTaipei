from QuantLib import *
#import QuantLib as ql
import pandas as pd

effective_date = Date(1, 1, 2015) 
termination_date = Date(1, 1, 2016)
tenor = Period(Monthly)
calendar = UnitedStates()
business_convention = Following
termination_business_convention = Following
date_generation = DateGeneration.Forward
end_of_month = False
schedule = Schedule(effective_date, termination_date, tenor, calendar, business_convention, termination_business_convention, date_generation, end_of_month)
pd.DataFrame({'date': list(schedule)})

annual_rate = 0.05
day_count = ActualActual()
compound_type = Compounded
frequency = Annual
interest_rate = InterestRate(annual_rate, day_count, compound_type, frequency)
print(interest_rate)

t = 2.0
print(interest_rate.compoundFactor(t))
print((1+annual_rate)*(1.0+annual_rate))


