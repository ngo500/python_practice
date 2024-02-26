"""
Module file with functions for getting the area of a rectangle and the area of a circle
"""

from math import pi

def area_of_rectangle(length, width):
    """
    Takes the length and width of a rectangle and returns area
    """
    return length * width

def area_of_circle(radius):
    """
    Takes the radius of a circle and returns area
    """
    return pi * radius ** 2
