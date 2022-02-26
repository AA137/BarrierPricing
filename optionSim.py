from matplotlib.pyplot import bar
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