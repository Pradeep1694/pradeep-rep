def prime_number(num):
    for i in range (2 ,num,1):
        if  (num % i ==0):
            print(f"{num} is not prime number")
            break
        elif i ==num-1:
            print(f"{num} is prime number")
prime_number(37)     