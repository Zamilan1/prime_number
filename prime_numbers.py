#This code checks if a given number is prime number or not.A prime number is natural
    #number greater than 1 has no positive  divisors other than 1 and itself. 
def is_prime(n):
    # if n less then 1 return flase
    if n <= 1:
        return False
    #if n equals to 2 return true
    if n == 2:
        return True
    #check for add numbers
    #if the number can be divided evenly by any odd number, it's not a prime number
    #so we just need to check till square root of that number
    
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        # if n is divisible by i ,then it is not a prime number
        if n % i == 0:
            return False
        
    return True

def main():
    
    number = int(input("Enter a number: "))
    #if is prime number print out statement
    if is_prime(number):
        print(f"{number} is a prime number.")
        #or  you can use this way also
        #print("The number is prime")
    else:  #else  print out statement that is not prime number
        print(f"{number} is not a prime number.")

if __name__ == "__main__":
    main()
