try:
    num1,num2=eval(input("enter 2 numbers seperated by commas: "))
    result=num1/num2
except ZeroDivisionError as ex:
    print(f"Math error!!: {ex}")
except SyntaxError as ex:
    print(f"Please put a comma: {ex}")
except ValueError as ex:
    print(f"Error: {ex}, please enter an interger i.e(1,2,3,...)")