def add(a,b):
    return a+b
def diff(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b

a=int(input("ENTER THE FIRST VALUE:\n"))
b=int(input("ENTER THE SECOND VALUE:\n"))



while True:

    print("EL MENU,\n1:Addition,\n2:Subtraction,\n3:Multiplication,\n4:Division,\n5:Exit\n")

    c=int(input("ENTER THE OPTIONS FOR OPERATION:\n"))

    if c==1:
        print('addition:',add(a,b))
        
    elif c==2:
        print('subtraction:',diff(a,b))
        
    elif c==3:
        print('multiplication:',multi(a,b))
        
    elif c==4:
        print('division:',div(a,b))
        
    else:
        print('~~~~~exit~~~~~')
        break
        
