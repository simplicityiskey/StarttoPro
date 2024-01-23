#Ex 94: is it a valid triangle 
'''Write a function that determines whether or not three lengths can forma triangle. 

The result will take 3 results and returna Boolean value.

If any length is less than or equal to 0 thn the result will return false.




in addition write a program that reads 3 lengths forrm the user and demonstrats the behaviour of the function. 
'''


#Choose 3 numbers from the user. 
#Assign the 3 numbers to 3 variables
#If any of the variables equal 0 or are less than 0 then immediately return false.
#Find out the order of the variables
#If the two smaller lengths are equal or lss than th other side then it cannot be a triangle 
#As long as it fits these then it can be a triangle


def valid_triangle():x = int(input('What is your first number '))
y = int(input('what is your second number '))
z = int(input('What is your third number '))

if (x or y or z == 0):
    print('nope')
    break

else:
    continue
    
case = [x, y, z]
case.sort()

if (case[0]+case[1])<case[2]:
    print('nope')
    
else:
    print ('there we go')

print(case)




