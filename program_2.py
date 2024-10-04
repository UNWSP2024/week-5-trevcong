#AUTHOR: Trevor Conger UNWSP
#DATE: 10/4/24
#TITLE: 2 random numbers, can you add them up?
import random


#Main, Only should call addTwoRandomNumbers
def main():
    addTwoRandomNumbers()

#Two random numbers will be generated 1 through 500
#User needs to add the numbers, if they are correct the program will end, if not they will need to keep trying
#RETURN: print statement Correct with randAnswer
def addTwoRandomNumbers():
    rand1 = random.randint(1, 500)
    rand2 = random.randint(1, 500)
    randAnswer = rand1 + rand2
    while(True):
        try:
            print("  ", rand1)
            print("+ ", rand2)
            print("=  ?")
            userInput = input("What is the sum of these two numbers: ")
            if int(userInput) == randAnswer:
                print("Congrats! You gave the answer:", randAnswer)
                break
            else:
                print("This is not correct")
        except ValueError:
            print(ValueError, " : We would like an integer!")
    print("")

if __name__ == "__main__":
    main()
