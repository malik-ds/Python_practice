#If-Else conditions

name='Alice'
if name=='Alice':
    print('Welcome Alice.')
else:
    print('Hey, stranger!')


# If Elif Else condition.

name=input('Enter your name : ')
age=int(input('Enter your age : '))
if name=='Dude' and age == 15:
    print('Welcome Dude.')
elif name =='Dude' and age < 15:
    print('You are not Dude, Kiddo.')
elif name=='Dude' and age != 15:
    print('You are not Dude.')
else:
    print('Hey '+name+', You are '+str(age)+' year old.')
    
