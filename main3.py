try:
    num=int(input("enter your age: "))
    if num>=18:
        print("sucess")
    else:
        print("false")
except ValueError as ex:
    print(f"Error: {ex}, please enter an interger i.e(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,...)")