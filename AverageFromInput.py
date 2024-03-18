#cs175L
#Miriam Abecasis
#average from input
def main():
    total_lines = 0
    total_num = 0
    try:
        infile = open ('numbers.txt' , 'r')
        #read values
        for line in infile:
            try:
                total_num += int(line)
                total_lines += 1
                print(f'I read in {total_lines} number(s) Current number is: {float(line):.2f} Total is: {total_num:.2f}')
            except ValueError:
                print(f'Bad data: {line.strip()} skipping')
        print(f'Average: {(total_num / total_lines)}')
    except IOError:
        print("File not found: numbers.txt - exiting")
    #except ValueError:
     #   print(f'Bad data: {line} skipping')

if __name__ == '__main__':
    main()
