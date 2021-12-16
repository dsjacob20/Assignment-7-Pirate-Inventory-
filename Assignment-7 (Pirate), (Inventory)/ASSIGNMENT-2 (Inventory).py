

from os import truncate


inventory = {}
order = {}


#Adds to inventory
def add(i, n, q):
    if n in i:
        current = i[n]
        i[n] = current + q
    else:
        i[n] = int(q)

#subtracts from inventory
def sub(o, i, n, q):
    o[n] = int(q)
    current = i[n]
    i[n] = current - int(q)
    if i[n] < 0:
        print("We unfortunitly do not have that many in stock!")
        print("Please redo your order!" )
        i[n] = current + int(q)
        del o[n]
        a = "y"
    else:
        print("     Your Order has been placed!")
        print("     Please pick-up in store!")
        a =  "n"
    return a


#Clears the screen
def clear_screen():
    import os
    os.system('cls')


clear_screen()

loop = True
while loop == True:
    #welcome message
    print()
    print('\t', "Welcome to 🐾BAMAZONE!🐾")
    print('\t', "'Your House is Our House!!!'")
    print()
    print("If you are a CUSTOMER enter - 1")
    print("EMPLOYEE enter - 2")
    c = input("       # ")
    clear_screen()
    print()

    #Employee
    if c == "2":
        print("1 - add to inventory")
        print("2 - view inventory")
        c = input("       # ")
        clear_screen()
        print()

        #ADDS to inventory
        if c == "1":
            loop = True
            while loop==True:
                print("To finish updating Enter - 'c' for name")
                print()
                n = input ("    Name of product: ")
                n = n.lower()
                if n in ('c'):
                    loop = False
                    clear_screen()
                    print()
                else:
                    q = input("    Quantity of product: ")
                    if q == "":
                        q = 0
                    else:
                        q = q
                    add(inventory , n, q)
                    clear_screen()
                    print()
                    x = (inventory.get(n))
                    print("    Inventory updated!   '", n, ":", x, "'")
                    print("             ----------")
            print("UPDATED INVENTORY; ")
            print()
            for all in inventory.keys():
                print ('\t',"{:<15}:{:>10}".format(all, inventory[all]))
            print()

        #views inventory
        elif c == "2": 
            for all in inventory.keys():
                print ('\t',"{:<15}:{:>10}".format(all, inventory[all]))
            print()

    #CUSTOMER
    elif c == "1":
        loop = True
        while loop==True:
            #search
            print()
            print("                 ----------")
            print("If you have something specific in mind then enter there.")
            print("If you would like to see the inventory then just press Enter.")
            print("To see your ORDERS enter - 1")
            print("                 ----------")
            e = input("     Search: ")
            clear_screen()
            print()
            #To see inventory
            if e == "":
                print("INVENTORY;")
                print()
                print ('\t',"{:<15}:{:>13}".format("NAME", "QUANTITY"))
                for all in inventory.keys():
                    print ('\t',"{:<15}:{:>10}".format(all, inventory[all]))
                print()
                e = input(" So what would you like to buy: ")
                if e in inventory:
                    x = (inventory.get(e))
                    clear_screen()
                    print()
                    print ('\t',"{:<15}:{:>10}".format(e, x))
                    print()
                    print("We do have", e, " in stock!")
                    c = input("To cheakout? Press Enter!")
                    clear_screen()
                    print()
                    print("                 CHEAK-OUT")
                    print("                 ----------")
                    print()
                    n = e
                    print("Item name: ",n)
                    q = input("Quantity: ")
                    o = sub(order, inventory, n, q)
                    print("             ----------")
                    print()
                    if o == "y":
                        x = input("To restart the order press Enter!")
                        if x == "":
                            loop = True
                    elif o == "n":
                        print("To keep shopping press Enter!")
                        print("To Finish Enter - 1")
                        x = input("         # ")
                        if x == "1":
                            loop = False
                            clear_screen()
                            print()
                            #sees their orders
                            print("YOUR ORDER: ")
                            print()
                            print ('\t',"{:<15}:{:>13}".format("NAME", "QUANTITY"))
                            for all in order.keys():
                                print ('\t',"{:<15}:{:>10}".format(all, order[all]))
                        else:
                            loop = True
                #if what their search is not in inventory
                else:
                    print("The item you are looking for is currently available!")
                    print("Please try again!")
                    print()
                    n = input("Press enter to return to search!")
                    if n == "":
                        loop = True
                        clear_screen()
                    else:
                        print()
            else:
                print("🔎Search: ", e)
                e = e.lower()
                #What they searched for in inventory
                if e in inventory:
                    x = (inventory.get(e))
                    print()
                    print ('\t',"{:<15}:{:>10}".format(e, x))
                    print()
                    print("We do have", e, " in stock!")
                    c = input("To cheakout? Press Enter!")
                    #cheakout
                    clear_screen()
                    print()
                    print("                 CHEAK-OUT")
                    print("                 ----------")
                    print()
                    n = e
                    print("Item name: ",n)
                    q = input("Quantity:")
                    o = sub(order,inventory, n, q)
                    print("             ----------")
                    print()
                    if o == "y":
                        x = input("To restart the order press Enter!")
                        if x == "":
                            loop = True
                    elif o == "n":
                        print("To keep shopping press Enter!")
                        print("To Finish Enter - 1")
                        x = input("         # ")
                        if x == "1":
                            loop = False
                            clear_screen()
                            print()
                            #sees their orders
                            print("YOUR ORDER: ")
                            print()
                            print ('\t',"{:<15}:{:>13}".format("NAME", "QUANTITY"))
                            for all in order.keys():
                                print ('\t',"{:<15}:{:>10}".format(all, order[all]))
                        else:
                            loop = True
                elif e == "1":
                    print("YOUR ORDER: ")
                    print()
                    print ('\t',"{:<15}:{:>13}".format("NAME", "QUANTITY"))
                    for all in order.keys():
                         print ('\t',"{:<15}:{:>10}".format(all, order[all]))
                else:
                    print()
                    print("The item you are looking for is currently available!")
                    print("Please try again!")
                    print()
                    n = input("Press enter to return to search!")
                    if n == "":
                        loop = True
                        clear_screen()
                    else:
                        print()



    b = input("To return to main menu press ENTER")
    if b == "":
        loop = True
    else:
        print()
    clear_screen()
