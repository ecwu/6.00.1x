import math
#Math library should importing at the beginning of your code in order to call the tan function and to get the pi constant.

def polysum(n,s):
    '''
    n = number of sides
    s = Each side has length
    '''
    area = (0.25*n*s**2)/math.tan(math.pi/n)
    perimeter = (n*s)**2
    sum = float('%.4f' % (area + perimeter)) #rounded to 4 decimal places
    return sum