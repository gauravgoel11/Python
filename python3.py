code = 'khul ja simsim'
count = 0
maxcount = 3

for x in range(count, maxcount):
    user = input('please enter code')
    if user == code:
        print('you have enter right code')
        break
    elif user != code:
        print('you have enter  you have ' + str(2-x) + ' attempt left')
