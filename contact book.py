print("\n> > > > > > > > > > CONTACT BOOK < < < < < < < < < <")
d = {}
while  True:

    print("\nPRESS 1 TO ADD A CONTACT")
    print("PRESS 2 TO VIEW ALL CONTACT")
    print("PRESS 3 TO DELET CONTACT")
    print("PRESS 4 TO EDIT NAME")
    print("PRESS 5 TO EDIT MOBILE NUMBER")
    print("PRESS 6 TO EXIT CONTACT BOOK")
    choice = int(input("ENTER YOUR CHOICE :"))

    if choice == 1:
        print("\n> > > > > > > > > > ADD CONTACT < < < < < < < < < <")
        a = input("\nENTER THE NAME :")
        b = int(input("ENTER THE MOB NO :"))
        d[a]=b #this line adds the key:value TO the dict
        print("\nCONTACT ADDED SUCCESSFULLY")
    

    elif choice == 2:
        print("\n> > > > > > > > > > VIEW CONTACT < < < < < < < < < <")
        for a, b in d.items():
            print(a,b)
        if  not  d:
            print("\nCONTACT BOOK IS EMPTY..!!!")
        

    elif choice == 3:
        print("\n> > > > > > > > > > DELETE CONTACT < < < < < < < < < <")
        a = input("\nENTER THE EXISTING NAME :")
        if a in d:
            d.pop(a)
            print("\nDELETED SUCCESSFULLY")
        else:
            print("\nNAME NOT EXISTING..!!!")


    elif choice == 4:
        print("\n> > > > > > > > > > EDIT NAME < < < < < < < < < <")
        a = input("\nENTER THE EXISTING NAME :")
        if a in d:
            y = input("ENTER THE NEW NAME :")
            d[y] = d[a]
            del d[a]
            print("\nUPDATED SUCCESSFULLY")
        else:
            print("\nNAME NOT EXISTING..!!!")


    elif choice == 5:
        print("\n> > > > > > > > > > EDIT MOBILE NUMBER < < < < < < < < < <")
        a = input("\nENTER THE EXISTING NAME :")
        if a in d:
            x = int(input("ENTER THE NEW NUMBER :"))
            for x in d:
                print("\nNUMBER IS ALREADY EXISTING..!!!")
            else:
                d.update({a:x})
                print("\nUPDATED SUCCESSFULLY")
        else:
            print("\nNAME NOT EXISTING..!!!")


    elif choice == 6:
        print("\n> > > > > > > > > > CONTACT BOOK EXITED < < < < < < < < < <")
        print()
        exit()
    else:
        print("\nINVALID CHOICE")