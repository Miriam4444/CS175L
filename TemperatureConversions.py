def main():
    controlLoop()

def convertToKelvin():
    #Take in the fahrenheit temp as an argument
    getFahrenheit()
    #Convert Fahrenheit to Kelvin
    celsius = ((F_temp * 32) - 32) * (5/9)
    kelvin = celsius + 273
    #return Kelvin
    return kelvin
    #pass

def convertToCentigrade():
    #Take in the fahrenheit temp as an argument
    #F_temp = getFahrenheit()
    #Convert Fahrenheit to centigrade
    celsius = ((F_temp * 32) - 32) * (5/9)
    #return Centigrade
    return celsius
    #pass

def doConversion():
    #getFahrenheit(), get back Fahrenheit
    #F_temp = getFahrenheit()
    #convertToKelvin(), send Fahrenheit get back Kelvin
    kelvin = convertToKelvin()
    #ConvertToCentigrade, sends Fahrenheit gets back Centigrade
    celsius = convertToCentigrade()
    #prints for example: 'Fahrenheit: xx Kelvin xx Centigrade: xx'
    print(f'Fahrenheit: {F_temp :.2f} Kelvin: {kelvin :.2f} Centigrade: {celsius :.2f}')
    #pass

def repeat():
    #Inputs How many conversions would you like to do this time?
    how_many = int(input("How many conversions would you like to do this time? "))
    #for x in range how many
        #doConversion()
    for i in range(how_many):
        doConversion()
    #for x in range how many
        #doConversion()
    #pass

def controlLoop():
    #Inputs 'Do you want to do some conversions(Yes or No)?'
    conversions = input("Do you want to do some conversions(Yes or No)? ")
    #if 'yes' repeat()
    if conversions == "yes":
        repeat()
    #pass

def getFahrenheit():
    #Inputs 'Enter Fahrenheit temperature (must be -50 to 130):'
    F_temp1 = float(input("Enter Fahrenheit temperature (must be -50 to 130): "))
    #(validation loop)'Please re-enter'
    while True:
        if (F_temp1 <= -50) or (F_temp1 >= 130): 
            F_temp1 = float(input("Please re-enter "))
        else:
            break
    global F_temp
    F_temp = F_temp1
    #pass

# Call the main function.
if __name__ == '__main__':
    main()
