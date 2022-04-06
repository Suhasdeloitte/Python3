def calculator():
    try:
        print("\n")
        num1 = float(str(input("Please enter your first number: ")))

        num2 = float(str(input("Please enter your second number: ")))

        opp = input("Please enter an operation: +-*/   ")

        if opp == "+":
            ans = num1 + num2

        elif opp == "-":
            ans = num1 - num2

        elif opp == "*":
            ans = num1 * num2

        elif opp == "/":
            ans = num1//num2

        if(ans<0):
            print("negative answer!! enter valid inputs")
        else:
            print(f"Ans: {ans}")

    except:
        print("Formula Error")


    finally:
        value=str(input("Do you want to quit?: "))
        if value == "yes":
            quit()
        elif value == "no":
            calculator()
        else:
            print("invalid input")
    







calculator()

