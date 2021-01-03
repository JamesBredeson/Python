# simple input & output 
print ('Type your name') #prints statement
name = input() #you type your name
print('Your name is', name) #displays text and your name entered

print ('What is your age?')
age = input()
print(name , 'Your age is', age)

input("Press Enter to continue...")

print ("Multi-variable input")
input("Press Enter to continue...")

name = input('name: ')
age = input('age: ')
print ('hello', name, 'you are', age, 'years old')


input("Press Enter to continue...")

a_variable = 'I am a variable'
b_variable = 'I am also a variable'
dif_variable = 'Variables can be named anything except core values'

print (a_variable + b_variable + dif_variable)
input("Press Enter to continue...")
print ('as you see, using a + sign does not create a space in the print')
input("Press Enter to continue...")

print (a_variable, b_variable, dif_variable)
input("Press Enter to continue...")
print ('here we used , to seperate variables')

input("Press Enter to continue...")
print ('Arithmetic Operators')

x = input('type a number: ')
y = input('type another number: ')
result_1 = (int(x) + int(y))
result_2 = (int(x) - int(y))
result_3 = (int(x) * int(y))
result_4 = (int(x) / int(y))
result_5 = (int(x) **int(y))
result_6 = (int(x) % int(y))

print (result_1, 'This is ', x, '+', y)
print (result_2, 'This is ', x, '-', y)
print (result_3, 'This is ', x, '*', y)
print (result_4, 'This is ', x, '/', y)
print (result_5, 'This is ', x, '**', y)
print (result_6, 'This is ', x, '%', y)

input("Press Enter to continue...")

x = input('type a number: ')
y = input('type another number: ')
res_1 = (int(x) == int(y))
res_2 = (int(x) != int(y))
res_3 = (int(x) <= int(y))
res_4 = (int(x) >=int(y))
res_5 = (int(x) <int(y))
res_6 = (int(x) > int(y))

print ('are your numbers equal to each other?', res_1)
print ('are your numbers  NOT equal to each other?', res_2)
print ('is', x, 'less or equal to', y, res_3)
print ('is', x, 'greater or equal to', y, res_4)
print ('is', x, 'less than', y, res_5)
print ('is', x, 'greater than', y, res_6)
