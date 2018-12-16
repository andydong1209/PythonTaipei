from QuantLib import *
import numpy as np
import matplotlib.pyplot as plt

today = Date(7, March, 2014)
Settings.instance().evaluationDate = today

option = EuropeanOption(PlainVanillaPayoff(Option.Call, 100.0), 
	EuropeanExercise(Date(7, June, 2014)))
u = SimpleQuote(105.0)
r = SimpleQuote(0.01)
sigma = SimpleQuote(0.20)

riskFreeCurve = FlatForward(0, TARGET(), QuoteHandle(r), Actual360())
volatility = BlackConstantVol(0, TARGET(), QuoteHandle(sigma), Actual360())
process = BlackScholesProcess(QuoteHandle(u), 
	YieldTermStructureHandle(riskFreeCurve), 
	BlackVolTermStructureHandle(volatility))

engine = AnalyticEuropeanEngine(process)
option.setPricingEngine(engine)

print(option.NPV())

model = HestonModel(HestonProcess(YieldTermStructureHandle(riskFreeCurve), 
	YieldTermStructureHandle(FlatForward(0, TARGET(), 0.0, Actual360())), 
	QuoteHandle(u), 0.04, 0.1, 0.01, 0.05, -0.75))

engine = AnalyticHestonEngine(model)
option.setPricingEngine(engine)

print(option.NPV())
