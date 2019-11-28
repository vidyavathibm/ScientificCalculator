"""Test Cases for e_power_x"""
"""Test Cases for X_power_y"""
import unittest
from src.driver.scientific_calc import ScientificCalc

class ScientificCalcTest(unittest.TestCase):
    """functions are defined for checking the main cases"""

    def test_e_power_x_positive_exp(self):
        "When the input is positive integer"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(2), 2.71828182846 ** 2)

    def test_e_power_x_negative_exp(self):
        "When the input is negative integer"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(-2), 2.71828182846 ** -2)

    def test_e_power_x_zero_exp(self):
        "When the input is zero"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(0), 2.71828182846 ** 0)

    def test_e_power_x_pos_decimal_exp(self):
        "When the input is positive decimal"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(8.6), 2.71828182846 ** 8.6)

    def test_e_power_x_neg_decimal_exp(self):
        "When the input is negative decimal"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(-8.6), 2.71828182846 ** -8.6)

    def test_e_power_x_try_except(self):
        "Test case for try and except"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func('accenture'),
                         "Please enter float or integer types input.")

    def test_x_power_y_posint_posint(self):
        """When both the input is positive integer"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(2, 2), pow(2, 2))

    def test_x_power_y_negint_posint(self):
        """When power is positive integer and base is negative integer"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(-2, 2), pow(-2, 2))

    def test_x_power_y_negint_negint(self):
        """When both the input is negative integer"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(-2, -2), pow(-2, -2))

    def test_x_power_y_posint_negint(self):
        """When power is negative integer and base is positive integer"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(2, -2), pow(2, -2))

    def test_x_power_y_posfloat_posint(self):
        """When power is negative integer and base is positive float value"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(2.2, 2), pow(2.2, 2))

    def test_x_power_y_posfloat_negint(self):
        """When power is negative integer and base is positive float value"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(2.2, -2), pow(2.2, -2))

    def test_x_power_y_negfloat_posint(self):
        """When power is positive integer and base is negative float value"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(-2.2, 2), pow(-2.2, 2))

    def test_x_power_y_negfloat_negint(self):
        """When power is negative integer and base is negative float value"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(-2.2, -2), pow(2.2, -2))

    def test_x_power_y_string_num(self):
        """When power is positive integer and base is string"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization("string", 2), "Value Error")

    def test_x_power_y_num_string(self):
        """When power is string and base is positive integer"""
        test_obj = ScientificCalc()
        self.assertEqual(test_obj.var_initialization(2, "string"), "Value Error")

