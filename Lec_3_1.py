from QuantLib import *

today = Date(8, October, 2014)
Settings.instance().evaluationDate = today

option = BarrierOption(Barrier.UpIn, 120.0, # barrier 
	0.0, # rebate 
	PlainVanillaPayoff(Option.Call, 100.0), 
	EuropeanExercise(Date(8, January, 2015)))

u = SimpleQuote(100.0)
r = SimpleQuote(0.01)
sigma = SimpleQuote(0.20)

riskFreeCurve = FlatForward(0, TARGET(), QuoteHandle(r), Actual360())
volatility = BlackConstantVol(0, TARGET(), QuoteHandle(sigma), Actual360())
process = BlackScholesProcess(QuoteHandle(u), YieldTermStructureHandle(riskFreeCurve),
	BlackVolTermStructureHandle(volatility))
option.setPricingEngine(AnalyticBarrierEngine(process))

u0 = u.value(); h = 0.01
P0 = option.NPV()
print(P0)

u.setValue(u0+h)
P_plus = option.NPV()
print(P_plus)

u.setValue(u0-h)
P_minus = option.NPV()
print(P_minus)

u.setValue(u0)
Delta = (P_plus - P_minus)/(2*h)
Gamma = (P_plus - 2*P0 + P_minus)/(h*h)
print(Delta)
print(Gamma)

r0 = r.value() ; h = 0.0001
r.setValue(r0+h) ; P_plus = option.NPV()
r.setValue(r0)
Rho = (P_plus - P0)/h
print(Rho)

sigma0 = sigma.value() ; h = 0.0001
sigma.setValue(sigma0+h) ; P_plus = option.NPV()
sigma.setValue(sigma0)
Vega = (P_plus - P0)/h
print(Vega)

Settings.instance().evaluationDate = today+1
P1 = option.NPV()
h = 1.0/365
Theta = (P1-P0)/h
print(Theta)
