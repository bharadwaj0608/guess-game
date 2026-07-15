import random
orginal_number=random.randint(0,100)
while(True):
    try:
        value=int(input("Enter number "))
        if(value==orginal_number):
            print("you won")
            break
        elif(value>orginal_number):
            print("Smaller")
        elif(value<orginal_number):
            print("Bigger")
    except (KeyboardInterrupt,SyntaxError,ValueError):
        print("\nplease give valid input")

