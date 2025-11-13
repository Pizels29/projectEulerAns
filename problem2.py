def fibonacci():
    prev = 0
    num = 1
    sums = 0
    while num<4000000:
        prev,num = num,prev+num
        if num % 2 == 0:
            sums = sums + num
    return sums

print(fibonacci())
