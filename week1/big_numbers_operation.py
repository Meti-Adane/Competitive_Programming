
carry = 0
# sign check function
def sign_check(a, b):
    if a > 0 and b > 0:
        return 1
    elif a < 0 and b < 0:
        return 0
    elif a < 0 or b < 0:
        return -1

# if both numbers are equal longest digit function takes the first input as the longest
def longest_digit(a, b):
    if len(a) > len(b):
        return a
    elif len(b) > len(a):
        return b
    else:
        return a

#  if both numbers are equal in digit length then smallest digit function assumes the second number to be the smallest
def smallest_digit(a, b):
    if len(a) < len(b):
        return a
    elif len(b) < len(a):
        return b
    else:
        return b

def summation_operation(a, b):
    first_number = longest_digit(str(a), str(b))
    second_number = smallest_digit(str(a) , str(b))
    sum = ""
    carry = 0
    difference_in_digits = len(first_number) - len(second_number)
    zeros_required = "0" * difference_in_digits
    second_number = zeros_required + second_number

    for i in range(len(first_number) - 1, -1, -1):
        result = int(first_number[i]) + int(second_number[i]) + carry
        carry = result // 10
        sum = str(result) + sum
    return sum

def subtraction_operation(a, b):
    if a > b:
        first_number = str(a)
        second_number = str(b)
    elif b > a:
        first_number = str(b)
        second_number = str(a)
    else: return 0
    difference = ""
    borrow = 0
    difference_in_digits = len((first_number)) - len((second_number))
    zeros_required = "0" * difference_in_digits
    second_number = zeros_required + (second_number)
    difference_in_digits = len((first_number)) - len((second_number))
    zeros_required = "0" * difference_in_digits
    second_number = zeros_required + second_number

    for i in range (len((first_number)) - 1, -1, -1):
        if int(first_number[i]) < int(second_number[i]):
            borrow += 1
            temp_first_number = int(first_number[i]) + 10
            difference = str(temp_first_number - int(second_number[i])) + difference
        elif int(first_number[i]) >= int(second_number[i]):
            difference = str(int(first_number[i]) - int(second_number[i]) - borrow) + difference
            borrow = 0
    return difference

def multiplication_operation(a, b):
    first_number = longest_digit(str(a), str(b))
    second_number = smallest_digit(str(a), str(b))
    intermidiate_products=[]
    for j in range(len(second_number) - 1, -1, -1):
        product = ""
        carry = 0
        for i in range(len(first_number)-1, -1, -1):
            result = int(second_number[j]) * int(first_number[i]) + carry
            carry = result // 10
            product = str(result % 10) + product
            # print(result, carry, product)
        required_zeros = "0" * (len(second_number)-1 - j)
        product1 = str(carry) + product + required_zeros

        intermidiate_products.append(product1)
    i = 0
    p = 0
    if len(intermidiate_products) % 2 != 0:
       intermidiate_products.append(0)

    while i <= len(intermidiate_products)-1:
        # use your iwn code here
        l = int(summation_operation(intermidiate_products[i], intermidiate_products[i+1]))
        p = summation_operation(p, l)
        i+=2
    return p

def multiply(a, b):
    result = 0
    if sign_check(a, b) == 1:
        result = multiplication_operation(a, b)
    elif sign_check(a, b) == 0:
        a = int(a) * -1
        b = int(b) * -1
        result = multiplication_operation(a, b)
    elif sign_check(a, b) == -1:
        if a < 0:
            a = int(a) * -1
        elif b < 0:
            b = int(b) * -1
        result = int(multiplication_operation(a, b)) * -1
    return result

def add(a, b):
    result = 0
    if sign_check(a, b) == 1:
        result = int(summation_operation(a, b))
    elif sign_check(a, b) == 0:
        a = int(a) * -1
        b = int(b) * -1
        result = int(summation_operation(a, b)) * -1
    elif sign_check(a, b) == -1:
        if a < 0:
            a = int(a) * -1
        elif b < 0:
            b = int(b) * -1
        result = (subtraction_operation(a, b))
    return result


n = 33
m = 333
print(add(n , m))
print(323 + 333)
# print(summation(1000000, 1000000))
# print(10^1000000000 + 10^1000000000)

