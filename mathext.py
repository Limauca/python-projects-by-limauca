from math import *

def area(a, b):
    return round(a*b, 14)

def triarea(a, b):
    return round(a*b/2, 14)

def sqarea(a): 
    return round(a**2, 14)

#math has sqrt
def sq(a):
    return round(a**2, 14)

#math has cbrt
def cb(a):
    return round(a**3, 14)

#matg has pow(number,exponent)
def power(a, b):
    return round(a**b, 14)

def root(a, b):
    return round(a**(1/b), 14)

#pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
#edit by cute_hitoya
#math has a exact value of pi

def pythag_a_b(a, b):
    return root(a**2 + b**2, 2)

def pythag_a_c(a, c):
    return root(c**2 - a**2, 2)

def pythag_b_c(b, c):
    return root(c**2 - b**2, 2)

def inch_feet(inch):
    return round(inch * 12, 14)

def feet_inch(feet):
    return round(feet / 12, 14)

def feet_yards(feet):
    return round(feet * 3, 14)

def yards_feet(yards):
    return round(yards / 3, 14)

def mile_yards(mile):
    return round(mile * 1760, 14)

def yards_mile(yards):
    return round(yards / 1760, 14)

def metric_table():
    print("\n | Meter = 100 centimeters, 10 decimeters or 1000 millimeters \n | Kilometer = 1000 meters")


#hi this cute_hitoya you can use better namings
  
