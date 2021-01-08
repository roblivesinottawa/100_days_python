# num = int(input("enter integer to check whether it's a prime number: "))

# if num > 1:
#     for n in range(2, num):
#         if num % n == 0:
#             print(f"{num} isn't a prime number.")
#             print(f"{n} times {num//n} is {num}")
#             break
#     else:
#         print(f"{num} is a prime number.")

# else:
#     print(f"{num} isn't a prime number.")




# # ask user to enter an integer
# num = int(input("check this integer: "))
# # create a function to calculate if integer is prime or not
# # pass the user's input as the parameter
# def prime_checker(n=num):
# # prime number can only be divided by 1 and itself
# # any number smaller than 1 can't be prime
#     if n <= 1:
#         return f"{n} isn't a prime number."
# # if number isn't smaller than 1 we can check whether it's prime
# # we use range to calculate from 2 up to number input by user
#     else:
#         for num in range(2, n):
# # if the number divided by itself isn't equal to 0
# # it's a prime number
#             if n % num == 0:
#                 return f"{n} isn't a prime number."
#     return f"{n} is a prime number."

# # call the function
# print(prime_checker())



def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            return f"{num} is not a prime"
    else:
        return f"{num} is a prime"


_num = int(input("check this integer: "))
print(is_prime(num=_num))