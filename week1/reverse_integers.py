def inverse_nums(x):
    inverse_holder=""
    if x < 0:
        # convert to positive
        x *= -1
        string_value = str(x)
        for i in range(len(string_value) - 1, -1, -1):
            inverse_holder += string_value[i]
        if ((-2 ** -31)) <= int(inverse_holder) <= ((2 ** 31) - 1):
            return int(inverse_holder) * -1
        return 0

    elif x >= 0:
        string_value= str(x)
        for i in range(len(string_value)-1, -1, -1):
            inverse_holder += string_value[i]
        if ((-2 ** -31)) <= int(inverse_holder) <= ((2 ** 31) - 1):
            return int(inverse_holder)
        else:
            return 0


n = 0
print(inverse_nums(n))




