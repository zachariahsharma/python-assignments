#this asks a number that we know what the numbers are to get the greatest common factor 
def printWelcomeMessage():
    message = 'Welcome 2 my program to find the greatest common factor of 2 numbers'
    print(message)
    print('='* len(message))


def askfornumber():
    while True:
        print('Enter a number: ', end = '')
        number = int(input())
        return number
        if number < 0:
            break
        else:
            print('this number can\'t be used no minus numbers ')


#this function finds the factors of the 2 inputed numbers
def findfactors(number):
    list_number = []
    for factor in range(1,number+1):
        if number % factor  ==  0:
            list_number.append(factor)
    return list_number


# this will find the common factors then find the greatest common factor
def greatestcommon(number1, number2):
    commonlist = []
    for num1 in list_of_factors_1:
        for num2 in list_of_factors_2:
            if num1==num2:
                commonlist.append(num1)
    print(f'The Greatest Common Factor (GCF) of {number1} and {number2} is {commonlist[-1]}')



if __name__  ==  '__main__':
    printWelcomeMessage()
    number1 = askfornumber()
    # print(number1)
    number2 = askfornumber()
    # print(number2)
    list_of_factors_1 = findfactors(number1)
    # print(list_of_factors_1)
    list_of_factors_2 = findfactors(number2)
    # print(list_of_factors_2)
    greatestcommon(number1, number2)

