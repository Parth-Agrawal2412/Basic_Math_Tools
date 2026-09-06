

def even_odd_finder():
    num_01 = int(input("Enter a number: "))

    if (num_01%2 == 0):
        print(f"{num_01} is even")
    else:
        print(f"{num_01} is odd")

    print(f"There is multiplication table of {num_01}")
    for t in range(1 , 11):
        print(f"{num_01} x {t} = {num_01*t}")

def table_generator():
    num_02 = int(input("Enter your number: "))
    for i in range(11):
        print(f"{num_02} x {i} = {num_02*i}")
    print("Table completed")

def check_prime():
    num_03 = int(input("Enter a number: "))

    if num_03 <= 1:
        print(f"{num_03} is not a prime number")
    else:
        is_prime = True
        for i in range(2, num_03):   # check divisors
            if num_03 % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{num_03} is a prime number")
        else:
            print(f"{num_03} is not a prime number")
    
def sum_of_degits():
    num_04 = input("Enter a number: ")   # user enters number as string
    sum_of_digits = 0               # start with 0

    for digit in num_04:                 # loop through each character
        sum_of_digits = sum_of_digits + int(digit) # convert character to int and add

    print("Sum of digits:", sum_of_digits)

