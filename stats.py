"""
Aum Desai
Fall 2022
CS152B Project 03

This program is for Project 03. It containes functions that 
can be called by other modules for use.
"""

def sum(data):

    '''
    This function takes a list parameter and returns the float sum 
    of those numbers in that list.
    '''

    total = 0.0

    for i in data:

        total += i

    return total

#def test():
    
    '''
    This is a test function for the sum function.
    It takes no parameters.
    '''

    nums = [1,2,3,4]

    call = sum(nums)

    print(call)


#if __name__ == "__main__":
    test()


def mean(data):

    '''
    This function takes 1 paramater called data,
    and it calculates and returns the mean. 
    It takes floats and returns floats. 
    '''

    average = sum(data) / len(data)

    return average

def min(data):

    '''
    This function takes 1 paramater called data,
    and it calculates and returns the min value. 
    It takes floats and returns floats. 
    '''

    minimum = 9999

    for i in data:

        if i < minimum:

            minimum = i

    return minimum


def max(data):

    '''
    This function takes 1 paramater called data,
    and it calculates and returns the max value. 
    It takes floats and returns floats. 
    '''

    maximum = -9999

    for i in data:

        if i > maximum:

            maximum = i

    return maximum


def variance(data):

    '''
    This function takes 1 parameter called data,
    and it calculates the variance in that data.
    It takes a list and returns floats.
    '''

    diffs = []

    for i in data:

        diff = i - mean(data)

        diffs.append(diff**2)

    numerator = sum(diffs)

    denominator = len(data) - 1

    variance_value = float(numerator/denominator)

    return variance_value



#print("Variance is " + str(variance([1,2,3,4,5,6])))
#print("Max is " + str(max([1,2,3,4,5,6])))
#print("Min is " + str(min([1,2,3,4,5,6])))
#print("Sum is " + str(sum([1,2,3,4,5,6])))



