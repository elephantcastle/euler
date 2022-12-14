from functools import reduce

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


def lcmm(*args):
    return reduce(lcm, args)

result = lcmm(*range(1,21))
print(result)