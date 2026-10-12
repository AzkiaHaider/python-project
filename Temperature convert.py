print("Temperature converts")
print("1.celsius to fahrenheit")
print("2.fahrenheit to celsius")
choice=input("enter you choice:")
if choice=="1":
    c=input("enter celsius:")
    f=(c*9/4)+32
    print("fahrenheit:",f)
elif choice=="2":
    f=float(input("enter fahrenheit:"))
    c=(f-32)*4/9
    print("celsius:",c)
else:
    print("invalid choice")       
