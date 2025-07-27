"""
Aum Desai
Fall 2022
CS152B Lab 03

This program is for Lab 03. It containes functions that take a list of
numbers and return their sum.
"""

def sum(numbers):

    '''
    This function takes a list parameter and returns the float sum 
    of those numbers in that list.
    '''

    total = 0.0

    for i in numbers:

        total += i

    return total

def test():
    
    '''
    This is a test function for the sum function.
    It takes no parameters.
    '''

    nums = [1,2,3,4]

    call = sum(nums)

    print(call)


if __name__ == "__main__":
    test()




