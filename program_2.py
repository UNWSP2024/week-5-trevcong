import random

def main():
    func()


def func():
    rand1 = random.randint(1, 500)
    rand2 = random.randint(1, 500)
    randAnswer = rand1 + rand2
    bool = True 
    while(bool):
        try:
            print("  ", rand1)
            print("+ ", rand2)
            print("=  ?")
            userInput = input("What is the sum of these two numbers: ")
            if int(userInput) == randAnswer:
                print("Congrats! You gave the answer ", randAnswer)
                break
            else:
                print("No")
        except:
            print("Nope")
    print("")

if __name__ == "__main__":
    main()
