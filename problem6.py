def sumofsquares(x):
    squares = x*(x+1)*(2*x+1)
    squares = squares/6
    return int(squares)
def squareofsums(y):
    sums = y*(y+1)
    sums = sums/2
    sums = sums**2
    return int(sums)
def difference(a):
    return squareofsums(a) - sumofsquares(a)
print(difference(100))
