#%matplotlib inline
from QuantLib import *
import numpy as np
import matplotlib.pyplot as plt

Settings.instance().evaluationDate = Date(3, October, 2014)

helpers = [ SwapRateHelper(QuoteHandle(SimpleQuote(rate/100.0)),
	Period(*tenor), TARGET(), Annual, Unadjusted, Thirty360(), Euribor6M())
for tenor, rate in [((2,Years), 0.201), ((3,Years), 0.258), ((5,Years), 0.464),
	((10,Years), 1.151), ((15,Years), 1.588)] ]

curve1 = PiecewiseFlatForward(0, TARGET(), helpers, Actual360())
dates, rates = zip(*curve1.nodes())
curve2 = ForwardCurve(dates, rates, Actual360())

times = np.linspace(0.0, 15.0, 400)
rates = [ curve1.zeroRate(t, Continuous).rate() for t in times ]

Settings.instance().evaluationDate = Date(19, September, 2014)
print("{0} to {1}".format(curve1.referenceDate(), curve1.maxDate()))
print("{0} to {1}".format(curve2.referenceDate(), curve2.maxDate()))

print(curve1.zeroRate(5.0, Continuous))
print(curve2.zeroRate(5.0, Continuous))

print(curve1.zeroRate(Date(7, September, 2019), Actual360(), Continuous))
print(curve2.zeroRate(Date(7, September, 2019), Actual360(), Continuous))

def make_observer(i):
	def say():
		s = "Observer %d notified" % i
		print('-'*len(s))
		print(s)
		print('-'*len(s))
	return Observer(say)

obs1 = make_observer(1)
obs2 = make_observer(2)

q1 = SimpleQuote(1.0)
obs1.registerWith(q1)

q2 = SimpleQuote(2.0)
obs2.registerWith(q2)

q3 = SimpleQuote(3.0)
obs1.registerWith(q3)
obs2.registerWith(q3)

q1.setValue(1.5)
q2.setValue(1.9)
q3.setValue(3.1)

obs1.registerWith(curve1)
obs2.registerWith(curve2)

Settings.instance().evaluationDate = Date(23, September, 2014)

