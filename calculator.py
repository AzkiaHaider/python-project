a=45
b=60
print(a+b)
print(a-b)
print(a/b)
print(a%b)
class calculator:
    def add(self,a,b):
        return a+b
    def subtract(self, a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def devision(self,a,b):
        return a/b
    def rem(self,a,b):
        return a%b

    ##CALCULATOR ................
    #calculator
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    choice = int(input("enter your choice"))
    if choice==1:
        print("Solution = ", num1+num2)
    elif choice==2:
        print("Solution =",num1-num2)
    elif choice==3:
        print("Solution= " , num1/num2)
    elif choice==4:
        print("Solution= " , num1%num2)