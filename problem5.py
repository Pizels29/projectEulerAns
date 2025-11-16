def gcd(a, b):
    while b != 0:
        a, b = b, a % b #used euclid's algorithm for this thx @the wagon dragon
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def result(x,y):
    result = 1
    for i in range(x, y):
        result = lcm(result, i)
    return result

print(result(1,21))

