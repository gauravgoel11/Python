try:
    # number = 10/0
    number = int(input('enter your number : '))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print('you have enter something wrong')
