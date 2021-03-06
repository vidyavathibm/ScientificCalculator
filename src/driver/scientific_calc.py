"""This module is to execute scientific calculator functions"""
import math
import logging
logging.basicConfig(filename='ScientificCalculatorLog.log', level=logging.ERROR,
                    format='%(name)s - %(levelname)s - %(message)s - %(asctime)s '
                           '- %(lineno)d - %(module)s - %('
                           'funcName)s - %(pathname)s')


class ScientificCalc:
    """This class is used to calculate the scientific operations"""


    def __init__(self):
        self.power = 0
        self.result = 0
        self.base = 0
        self.angle = 0
        self.tanhx = 0
        self.n_value = 0
        self.x_value = 0
        self.degree = 0
        self.radian = 0
        self.number = 0

    @classmethod
    def cal_power_ten(cls, pow_value):
        """This function is used to calculate ten power x value"""
        try:
            cls.answer = 10**float(pow_value)
            return cls.answer
        except ValueError as value_error:
            logging.error(value_error)
            raise ValueError

    @classmethod
    def exponential_func(cls, power_value):
        """This function is used to calculate the exponential function"""
        try:
            cls.power = float(power_value)
            exp_value = 2.71828182846
            cls.result = exp_value ** cls.power
            return cls.result
        except ValueError as error:
            logging.exception(error)
            print(error)
            return "Please enter float or integer types input."

    @classmethod
    def x_power_y(cls, base_val, power_val):
        """if power value is 0 returns 1
        else recursively calls x_power_y function and returns the final answer"""
        cls.answer = 1
        if power_val == 0:
            return 1
        elif power_val % 2 == 0:
            return (cls.x_power_y(base_val, int(power_val / 2)) *
                    cls.x_power_y(base_val, int(power_val / 2)))
        else:
            if power_val > 0:
                return (base_val * cls.x_power_y(base_val, int(power_val / 2)) *
                        cls.x_power_y(base_val, int(power_val / 2)))
            else:
                return (cls.x_power_y(base_val, int(power_val / 2)) *
                        cls.x_power_y(base_val, int(power_val / 2))) / base_val

    @classmethod
    def var_initialization(cls, base_no, power_no):
        """initializing the variables"""
        try:
            base = float(base_no)
            power = int(power_no)
            return cls.x_power_y(base, power)
        except ValueError as error:
            logging.exception(error)
            return "Value Error"

    @classmethod
    def calculate_tanh(cls, angle):
        """A method to calculate tanh"""
        try:
            cls.angle = angle
            cls.angle = float(cls.angle)
            exponential = math.e
            coshx = ((exponential ** cls.angle) + (exponential ** -cls.angle))
            sinhx = ((exponential ** cls.angle) - (exponential ** -cls.angle))
            cls.tanhx = sinhx / coshx
            return cls.tanhx
        except ValueError as error:
            logging.exception(error)
            return "value error(enter a number)"

    @classmethod
    def sin_func(cls, angle):
        """This function is used to calculate the sin function"""
        try:
            cls.value = math.sin(float(angle))
            return cls.value
        except ValueError as error:
            logging.exception(error)
            print(error)
            return "Please enter float or integer types input."

    @classmethod
    def cube_root(cls, n_value):
        """function"""
        try:

            v_value = int(n_value)
            if v_value > 0:
                return v_value ** (0.33333333333333333333333333333333)

            if v_value < 0:
                return -(-v_value) ** (0.33333333333333333333333333333333)

        except ValueError:
            logging.error(ValueError)
            return "ValueError"

    @classmethod
    def square_root(cls, x_value):
        """function for calculating square root"""
        try:
            cls.x_value = int(x_value)
            if cls.x_value >= 0:
                return cls.x_value ** 0.5
            elif cls.x_value < 0:
                imaginary_no = complex(cls.x_value) ** 0.5
                return imaginary_no
        except ValueError:
            logging.error(ValueError)
            return "expecting integer value"

    @classmethod
    def rad(cls, angle):
        '''calculate radians'''

        try:
            cls.degree = float(angle)
            constpi = math.pi
            cls.radian = cls.degree * (constpi / 180)
            return cls.radian
        except ValueError as ex:
            logging.error(ex)
            return "Value Error"

    @classmethod
    def one_by_x(cls, number):
        """returns 1/x"""
        try:
            return float(1) / float(number)
        except ZeroDivisionError:
            logging.warning("division with zero cannot be performed")
            return "ZeroDivisionError"
        except ValueError:
            logging.warning("give an integer")
            return "ValueError"

    @classmethod
    def calculate_cos(cls, angle):
        '''
        Function to calculate Cosine of an angle
         '''
        try:
            cls.angle=float(angle)
            cls.result = math.cos(cls.angle)
            return cls.result
        except ValueError as error:
            logging.exception(error)
            print(error)
            return "Please enter float or integer types input."
