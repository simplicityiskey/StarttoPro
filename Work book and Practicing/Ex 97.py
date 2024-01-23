#Write a function name precedence tha returns an integer representing the precedence of a athematical operator.

#A string containing the opertor will be passed to the function as its only parameter.

#My function should return 1 for +, 2 for -, 3 for *, 4 for /

# if there is no opertor then it should return -1

# Include a main program that will only run when the fil containing the solution has not been imported into nother program



#declare a function 'precedence'
#check for a single string input. 
#if it is one of them then return the respective number 
#if it is not one of them then i should return -1 
#main if __name__ = "__main__"
#main()

def precedence(x):
    if x == '+' or '-':
        return 1
    elif x == '/' or '*': 
        return 2
    elif x == '^': 
        return 3
    else:
        return -1
        
if __name__ == '__main__':
    print(precedence('dfckjvj'))