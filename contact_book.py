contact={}
while True:
    print("1. add contact")
    print("2. view contact")
    print("3. delete contact")
    print("4. update contact")
    print("5. exit contact")
    choice =int(input("enter choice:"))
    if choice==1:
        name=input("enter name:")
        phone=int(input("enter phone:"))
        contact[name]=phone
        print("contact add")
    elif choice==2:
        name=input("enter name:")
        if name in contact:
            print(contact[name])
        else:
            print(f"{name} doesn't exist")
    elif choice==3:
        name=int(input("enter name to delete:"))
        if name in contact:
            phone=int(input("enter new phone:"))
            del contact[name]
            print("contact deleted")
        else:
            print("contact cannot find")
    elif choice==4:
        name=int(input("enter name to update:"))
        if name in contact:
            phone=int(input("enter new phone:"))
            del contact[name]
            print("contact update")
        else:
            print("contact not found")
    elif choice==5:
        print("contact exit")
        break                    
