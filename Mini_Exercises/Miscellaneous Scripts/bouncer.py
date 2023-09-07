#ask for age
age = input('How old are you: ')

if age != "":
    age = int(age)
    if age >= 21:
        print ('you are good to enter and can drink')
    elif int(age) >= 18:
        print('You can enter, but need a wristband')
    else:
        print('you can\'t come in little one')
else:
    print('Please enter a valid age')

#less efficient method
'''if age != "":
    age = int(age)
    if age >= 18 and age < 21:
        print('You can enter, but need a wristband')
    elif int(age) >= 21:
        print ('you are good to enter and can drink')
    else:
        print('you can\'t come in little one')
else:
    print('Please enter a valid age')'''