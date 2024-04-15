#CS175L
#Miriam Abecasis
#Expense Pie Chart

#import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#define main function
def main():

    #make dictionary with key = expense and value = price of expense
    expense_dict = {}

    #try/except for IO error (if file isn't found)
    try:
        #open file
        file = open('expenses.txt' , 'r')

        #read each line in file and strip the new line and split into a list with 2 things
        for line in file:
            line = line.rstrip()
            categories = line.split("\t")

            #try/except for Value eror
            try:
                #add expense and price to dictionary as key value pair and make value into int
                expense_dict[categories[0]] = int(categories[1])
            except ValueError:
                print("non-integer value")

        #make a list of categories
        list_categories = list(expense_dict.keys())
        #make a list of values
        list_values = list(expense_dict.values())

        #make pie chart
        plt.pie(list_values , labels = list_categories)
        plt.show()

    except IOError:
        print("File not found")
#run function
if __name__ == '__main__':
    main()
