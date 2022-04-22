from matplotlib.pyplot import bar
import numpy as np
from numpy.polynomial import Polynomial
import pathSim
def european_style(price_arr, strike, barrier, long = True, knock_in  = True):
    if long:
        if knock_in:
            if max(price_arr) > barrier:
                return max(0, 100 * (price_arr[-1] - strike))
            else:
                return 0
        else:
            if max(price_arr) > barrier:
                return 0
            else:
                return max(0, 100 * (price_arr[-1] - strike))
    else:
        if knock_in:
            if min(price_arr) < barrier:
                return max(0, 100 * (strike - price_arr[-1]))
            else:
                return 0
        else:
            if min(price_arr) < barrier:
                return 0
            else:
                return max(0, 100 * (strike - price_arr[-1]))
def american_style(price_arr, strike, barrier, rho, long = True, knock_in  = True):
    if long:
        if knock_in:
            if max(price_arr) > barrier:
                return max(0, 100 * longstaff_schwartz_american_option_quadratic(price_arr,rho**(1/252), strike))
            else:
                return 0
        else:
            if max(price_arr) > barrier:
                return 0
            else:
                return max(0, 100 * longstaff_schwartz_american_option_quadratic(price_arr,rho**(1/252), strike))
    else:
        if knock_in:
            if min(price_arr) < barrier:
                return max(0, -100 * longstaff_schwartz_american_option_quadratic(price_arr,rho**(1/252), strike))
            else:
                return 0
        else:
            if min(price_arr) < barrier:
                return 0
            else:
                return max(0, -100 * longstaff_schwartz_american_option_quadratic(price_arr,rho**(1/252), strike))
def itm(payoff, spot):
    return payoff > 0
def ls_american_option_quadratic_iter(X, r, strike):
    # given no prior exercise we just receive the payoff of a European option
    cashflow = np.maximum(strike - X[-1], 0.0)
    # iterating backwards in time
    for i in reversed(range(1, len(X) - 1)):
        # discount factor between t[i] and t[i+1]
        df = np.exp(-r)
        # discount cashflows from next period
        cashflow = cashflow * df
        x = X[i]
        # exercise value for time t[i]
        exercise = np.maximum(strike - x, 0.0)
        # boolean index of all in-the-money paths
        itm = exercise > 0
        # fit polynomial of degree 2
        fitted = Polynomial.fit(x[itm], cashflow[itm], 2)
        # approximate continuation value
        continuation = fitted(x)
        # boolean index where exercise is beneficial
        ex_idx = itm & (exercise > continuation)
        # update cashflows with early exercises
        cashflow[ex_idx] = exercise[ex_idx]

        yield cashflow, x, fitted, continuation, exercise, ex_idx
def longstaff_schwartz_american_option_quadratic(X,r, strike):
    for cashflow, *_ in ls_american_option_quadratic_iter(X, r, strike):
        pass
    return cashflow.mean(axis=0) * np.exp(-r)
def simulate_american(num, spot, strike, dte, iv, barrier, rho, dt=0.05, long = True, knock_in = True):
    pass
    