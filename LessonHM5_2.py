'''
функція реалізації алгоритмів
розрахунку площі кола
'''

import math


def Area_of_circle(radius: int) -> int:

    '''

    :param radius: Radius
    :return: Area of circle
    '''

    try:
        s = math.pi * radius ** 2
    except Exception as error:
        return(f"It looks like something has happened. This is {error}")
    else:
        return s

print(Area_of_circle(radius = 5))