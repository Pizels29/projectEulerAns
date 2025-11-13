def sumthreeand5():
    num = 0
    sums = 0
    while num<1000:
        if num % 3 == 0 or num % 5 ==0:
            sums = sums + num
        num = num+1
    return sums
    
print(sumthreeand5())