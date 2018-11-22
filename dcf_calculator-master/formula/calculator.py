from __future__ import division
import math

def free_cash_flow(operating_income, tax_rate, dep_amort, cap_ex, adjustment=0):

    _nopat = nopat((operating_income - adjustment), tax_rate)

    return _nopat + dep_amort - cap_ex

def discount_free_cash_flow(free_cash_flow, discount_pct, year_index=0):
    """
        year_index
            e.g  0 for start year say 2015
            then 1 for 2016
                 2 for 2017 so on
    """
    discount_rate = (1 + (discount_pct/100))

    return free_cash_flow / math.pow(discount_rate, year_index)

def nopat(operating_income, tax_rate):
    """
        nopat = Net Operating Profit After Tax
    """
    return operating_income * (1-(tax_rate/100))

