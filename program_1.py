#AUTHOR: Trevor Conger UNWSP
#DATE: 10/4/24
#TITLE: Kilometer conversion!

#This function converts kilometers to miles
#RETURN: Miles as a float
def kilometer_conversion(kilometers):    
    miles = kilometers * .6214
    return miles

if __name__ == '__main__':
    userInp = float(input("Enter the number of kilometers: "))
    milesFromKilometers = kilometer_conversion(userInp)
    print("Your distance in miles is: ", milesFromKilometers)
    
