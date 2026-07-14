def prime(last_digit):
    list_of_primes = [2]    
    
    for number in range(3,last_digit+1):
        for divisor in range(2,number):
            if number % divisor == 0:
                break
        else:
            list_of_primes.append(number)
            
    return list_of_primes