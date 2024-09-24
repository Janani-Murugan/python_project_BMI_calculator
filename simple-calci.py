x=float(input())
y=float(input())
def add():
    print(x+y)
def subtract():
    print(x-y)
def mult():
    print(x*y)
def div():
    if y!=0:
        print(x/y)
    else:
        print("error!Division by zero is not allowed")

div()

add()
