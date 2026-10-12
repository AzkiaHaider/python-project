expense =[]

while True:

    print("__expense_tracker__")
    print("1.add expense")
    print("2.view expense")
    print("3.total expense")
    print("4.exit expense")

    choice=input("enter expense:")

    if choice=="1":
        name=input("enter expense:")
        amount=float(input("enter amount:"))
        expense.append([name,amount])
        print("expense added")


    elif choice=="2":
        print("__expense_tracker__")

        for var in expense:
            print(var[0],":",var[1])

    elif choice=="3":
        total=0

        for var in expense:
            total+=var[1]
        print("total expense:",total)
    elif choice=="4":
        print("exit expense")
        break
    else:
        print("not expense")    