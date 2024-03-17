#cs175L
#Miriam Abecasis
#average from input
def main():
    total_lines = 0
    total_num = 0
    infile = open ('numbers.txt' , 'r')
    #read values
    for line in infile:
        total_lines += 1
        total_num += float(line)
        print(f'I read in {total_lines} number(s) Current number is: {float(line):.2f} Total is: {total_num:.2f}')
    print(f'Average: {(total_num / total_lines)}')

if __name__ == '__main__':
    main()
