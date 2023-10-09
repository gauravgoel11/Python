def power(num1, num2):
    num3 = 1
    for x in range(0, num2):
        num3 = num1 * num3
    return num3


print(power(6, 0))
