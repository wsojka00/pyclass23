def prime_finder(num):
    primes=list()
    for i in num:
        x=0
        for j in range(1, i):
            if i%j == 0:
                x+=1
        if x==1:
            return True
        else:
            return False
