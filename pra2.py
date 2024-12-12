
# BIGGEST NUMBER

# x, y, z = 10, 20, 30

# if x > y and x > z:
#     print("X is bigger")

# elif y > x and y > z:
#     print("Y is bigger")

# else:
#     print("Z is bigger")


# PRIME NUMBER

# num = 7

# if num == 0 or num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             print(i, "times", num//i, "is", num)
#             break
#     else:
#         print(num, "is a prime number")

# # if input number is less than
# # or equal to 1, it is not prime
# else:
#     print(num, "is not a prime number")


# Write a programe to find weather the given number is PRIME NUMBER or not??

# num = int(input("Enter The Number"))

# if num == 0 or num == 1:
#     print(num, "Is not a prime number")
# elif num > 1:
#     for i in range(2, num-1):
#         if (num % i) == 0:
#             print(num, "Is not a prime number")
#     else:
#         print(num, "Is A Prime Number")


# Write a Python program to find prime numbers between 1 and 20 using a while loop.

# for i in range(2, 20):
#     j = 2
#     while (j <= (i/2)):
#         if (i % j == 0):  # factor found
#             break  # break out of while loop
#         j += 1
#     if (j > i/j):  # no factor found
#         print(i, "is a prime number")
# print("Bye Bye!!")

# for i in range(2, 20):
#     j = 2
#     while (j <= (i/2)):
#         if (i % j == 0):
#             break
#         j += 1
#     if (j > i/j):
#         print(i, "is a prime number")

# j = 2
# while j <= 20:
#     for k in range(1, 21):
#         if (j % k == 0):
#             break
#     else:
#         print(j, "Is a primenumber")
#     j += 1

# num = 1
# while num <= 10:
#     print("Hello")
#     num += 1


def add():
    a = int(input("Number 1"))
    b = int(input("Number 2"))
    c = (a + b)
    print(c)


add()


