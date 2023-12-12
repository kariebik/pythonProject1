import math
class Fraction:
    def __init__(self, numerator, denominator):
        hcf = math.gcd(numerator, denominator)
        self.numerator = numerator//hcf
        self.denominator = denominator//hcf
    def __repr__(self):
        return str(self.numerator) + '/' + str(self.denominator)
    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator
    def __add__(self, other):
        lcm = math.lcm(self.denominator, other.denominator)
        numer1 = (lcm//self.denominator) * self.numerator
        numer2 = (lcm//other.denominator) * other.numerator
        return Fraction(numer1+numer2, lcm)
    def __mul__(self, other):
        return Fraction(self.numerator*other.numerator, self.denominator*other.denominator)
    def __truediv__(self, other):
        return Fraction(self.numerator*other.denominator, self.denominator*other.numerator)
    def __sub__(self, other):
        lcm = math.lcm(self.denominator, other.denominator)
        numer1 = (lcm//self.denominator) * self.numerator
        numer2 = (lcm//other.denominator) * other.numerator
        return Fraction(numer1-numer2, lcm)

