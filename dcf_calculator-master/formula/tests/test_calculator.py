import unittest
from formula.calculator import free_cash_flow, nopat, discount_free_cash_flow

class TestDcfCalculatorYear2014(unittest.TestCase):

    def test_nopat(self):
        adjustment= 500
        _operating_income = 61800 - adjustment

        self.assertEquals(nopat(_operating_income, 0), 61300)

    def test_free_cash_flow(self):
        self.assertEquals(free_cash_flow(operating_income=61800,
                                    tax_rate=0,
                                    dep_amort=58100,
                                    cap_ex=62200,
                                    adjustment=500), 57200)


    def test_discount_free_cash_flow(self):
        _free_cash_flow = free_cash_flow(operating_income=61800,
                                    tax_rate=0,
                                    dep_amort=58100,
                                    cap_ex=62200,
                                    adjustment=500)

        self.assertEquals(discount_free_cash_flow(_free_cash_flow, 10, 0), 57200)

class TestDcfCalculatorYear2015(unittest.TestCase):

    def test_nopat(self):
        adjustment = 0
        _operating_income = 64054 - adjustment

        self.assertEquals(nopat(_operating_income, 0), 64054)

    def test_free_cash_flow(self):
        adjustment = 0
        _operating_income = 64054 - adjustment

        self.assertEquals(free_cash_flow(operating_income=_operating_income,
                                    tax_rate=0,
                                    dep_amort=52100,
                                    cap_ex=55000,
                                    adjustment=0), 61154)


    def test_discount_free_cash_flow(self):
        adjustment = 0
        _operating_income = 64054 - adjustment

        _free_cash_flow = free_cash_flow(operating_income=_operating_income,
                                    tax_rate=0,
                                    dep_amort=52100,
                                    cap_ex=55000,
                                    adjustment=0)

        self.assertEquals(discount_free_cash_flow(_free_cash_flow, 10, 1), 55594.54545454545)

