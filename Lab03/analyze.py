"""
Aum Desai
Fall 2022
CS152B Lab 03

This program is for Lab 03. It analyzes a csv file
and makes/prints a new list with data from the csv file. 
"""

import sys
import stats

def main(filename, column_id):

    '''
    This function simply opens a csv file for reading,
    and makes and prints a new list containing items from the csv file.
    It takes two command line parameters and returns a list of strings and floats.
    '''

    # assign to fp the result of opening the file hurricanes.csv for reading
    fp = open(filename, "r")

    # assign to line the first line of the data file
    line = fp.readline()

    # assign to headers the result of splitting the line using commas
    headers = line.split(",")

    # print headers
    print(headers)

    # assign to a list variable named data an empty list
    data = []

    # for all of the remaining lines in the file
    for line in fp:

        # assign to items the result of splitting the line using commas
        items = line.split(",")

        # append the second item to data (which index?) items cast as a float
        data.append(float(items[column_id]))

    # close the data file
    fp.close()

    # print data
    print(data)

    print(stats.sum(data))

    return


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))