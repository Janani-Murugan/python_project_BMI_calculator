def BMI():
    height=float(input())
    weight=float(input())
    age=int(input())
    x=weight/(height*height)
    print(x)
    if(x<18.5):
        print("underweight")
    elif(18.5<x<24.9):
        print("healthy range")
    elif(25<x<29.9):
        print("overweight")
    else:
        print("obesity")

BMI()
