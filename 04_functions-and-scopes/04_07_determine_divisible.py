# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages




def divisibleByFourOrSeven(num):
    
    
    """
    Checks if a number is divisible by four or seven and returns a bool
    """
    divisible = False
    
    if num % 7 == 0 or num % 4 == 0:
        divisible = True
        
    return divisible


def divisibleByFourAndSeven(num):
    
    
    """
    Checks if a number is divisible by four and seven and returns a bool
    """
    divisible = False
    
    if num % 7 == 0 and num % 4 == 0:
        divisible = True
    
    
    return divisible

big_num = input("Enter a number between one and a billion: ")

big_num = int(big_num)

seven_or_four = divisibleByFourOrSeven(big_num)
seven_and_four = divisibleByFourAndSeven(big_num)

print(f"That {str(big_num)} is divisible by four or seven is {seven_or_four}. \n That {str(big_num)} is divisible by four and seven is {seven_and_four}. \n")
