import math
 

def factorial(n):
    # print(math.factorial(23))
    value = 1
    for i in range(1, n+1):
        value = value * i
    return value

def sum_of_digit(n):
    value = 0
    for i in range(1, n+1):
        value = value + i
    return value

def reverse(n ):
    revd_number = 0  
    while (n > 0):  
        remainder = n % 10  
        revd_number = (revd_number * 10) + remainder  
        n = n // 10 
    return revd_number
    #recursion
    # if n==0:
    #     return r
    # else:
    #     return reverse(n//10, r*10 + n%10)


def check_is_strong_number(n):
     # 145 => (1)+ (1*2*3*4) + (1*2*3*4*5)
     # 1+24+120

    strong_num=0
    print("The number is")
    print(n)
    temp = n
    while(n > 0):
        remainder = n%10
        fact=factorial(remainder)
        strong_num = strong_num+fact
        n=n//10
    if(strong_num == temp):
        print("The number is a strong number")
    else:
        print("The number is not a strong number")

def is_armstrong_number(n):
     # 3*3*3 + 7*7*7 + 1*1*1 = 371
    arms_num=0
    temp = n
    while(n > 0):
        remainder = n%10
        arms_num = arms_num+ remainder**3
        n=n//10
        print(remainder**3)
    if(arms_num == temp):
        print("The number is a arm strong number")
    else:
        print("The number is not a arm strong number")

def is_palindrome_number(n):
    if(n == reverse(n)):
        print("The number is palindrome number")
    else:
        print("The number is not a palindrome number")

def add_btw_num(n1,n2):
    value = 0
    for i in range(n1,n2+1):
        value = value + i
    return value

def prime(n): # prime numner
    count = 0 
    for i in range(1, n):
        if(n % i == 0):
            count +=1
    if(count < 2): 
        return True
    return False


def prime_factor(target):
    for i in range(2, target+1):
        if(target % i == 0 and prime(i)): # find factor and which is Prime
            print(i)

if __name__ == '__main__':
    # print(factorial(5))
    # print(sum_of_digit(5))
    # print(reverse(675))
    print(add_btw_num(12,15))