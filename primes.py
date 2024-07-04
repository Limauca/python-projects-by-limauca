import time

def is_prime(a):
    y=0
    if a<0:
        a=a/-1
    if a<2:
        return False
    elif a in (2, 3, 5, 7, 11, 13):
        return True
    elif 0 in (a%2, a%3, a%5, a%7, a%11):
        return False
    else:
        x=5
        while x*x<a:
            if a%x==0 or a%(x+2)==0:
                return False
            x+=2
        return True

#z=[]
#y=0
x=1
start=time.time()
while x<=10000:
    print(" ", x, is_prime(x), "\n")
    x+=1
    #if is_prime(x):
        #y+=1
        #z.append(x)
end=time.time()
#print("    Found", y, "Primes")
#print("    Searched", x-1, "Primes")
#print(z)
print(" Time Elapsed:    ", end-start)
time.sleep(10)
