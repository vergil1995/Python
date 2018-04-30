import math
def polysum(n,s):
    area = (0.25*n*(s**2))/math.tan(math.pi/n)
    perimeter = n*s
    result = area + perimeter**2
    return round(result, 4)

print(polysum(82,36))