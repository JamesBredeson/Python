# printing results of numbers
print (15 + 10 +40)
print (10)
print (10*10)
# results of this print 65, 10, 100.

#/////////////

# Python print(15 + 10 + 40), but not 10*10
print (15 + 10 +40)
10
10*10
# This wont print either
15 + 10 + 40
10
10*10

#printing 5 to the third
print (5*5*5) 
# prints 125

#Saving Result
result = ('James')
print (result)

#variable names can be created
who = ('James')
some_number = (15 * 2 + 3)
print (who , some_number) #using text and integer use comma, cant use + with name and number
print (some_number + some_number) #integers can be be added, mut, divide, subtracted

# operators +=  -=  *=  /= **=
#we will replace this code  below with the operators
number = 20
print (number) #answer 20
print (number +15) #answer 35
#using operators
number = 7
number += 6
print (number) #7+6 = 13
x = 3
x *=3
print (x) #answer is 9, etc etc, point given on these operators
#note:  must have singular value fir otherwise this wont work
# y *=3  wont print, shows undefined
#y *=3
#print(y)
# this works
variable_1 = 5
variable_2 = 6
variable_2 += 10
variable_1 *= 4
print (variable_1, variable_2)

#at this point I want to make you press enter to continue code
input("Press Enter to continue...")

#prints numbers and nams
age = [21, 33, 47]
names = ('james', 'bill', 'tom')
animals = ["dog", "cat", 'mouse']
print (age)
print (names)
print (animals) #notice numbers do not have "" or ' '. also notice [] and () worked for name and animals

input("Press Enter to continue...")

message1 = "Whats up"
message2 = "James"
print (message1 + message2) # using + leaves no space
input("Press Enter to continue...")
print (message1 , message2) # using , leaves space
input("Press Enter to continue...")
print (message1 + "....." + message2) # using + "...." creates Whats up......James

input("Press Enter to continue...")

#creating a stored message and adding a result for it
msg = "Hello"
print (msg , "James") #msg is stored and using in the print, James is inputed

input("Press Enter to continue...")
#creating a paragraph

para = """  /alskdnfalkdsnfsdnfasonfas/ 
lknfas/dlknfds/lnfdlfnas/lknf/aslknf
/lkdsanflksdnflkajsnjdfndfjkankjndsfa
kjnasdjkfbnskjfbnaskjfbna/
sdjkfn   """ # notice we use THREE Quotes and press Enter for each new line
print (para)

input("Press Enter to continue...")
# making words bump to multiple lines usin \n
msg_1 = "Hi \n Bill \n this \n is \n James"
print (msg_1)

input("Press Enter to continue...")
#print the remainder of what is left over / i.e. 7 goes into 80, 11 times to make 77, 80-77 = 3
print (80 % 7)

input("Press Enter to continue...")

print ("What is your name")
name_1 = input()
print ("Hello", name_1)
print ("Type a number")
num1 = int(input())
print ("Type another number")
num2 = int(input())
print ("Equals", num1 + num2)

input("Press Enter to continue...")

print ("To Be Continued")