import first as f


def expresso():
    cost = f.MENU['espresso']['cost']
    quarter = int(input("How many quarters?"))
    dime =  int(input("How many dimes?"))
    nickle = int(input("How many nickels?"))
    cents =  int(input("How many cents?"))
    money_given = (0.25*quarter) + (0.1*dime) + (0.05*nickle) + (0.01*cents)

    if money_given > cost:
        f.resources['water'] = f.resources['water'] - 50
        f.resources['coffee'] = f.resources['coffee'] - 18
        return money_given - cost
    elif money_given == cost:
        f.resources['water'] = f.resources['water'] - 50
        f.resources['coffee'] = f.resources['coffee'] - 18
        return 0
    else:
        print("Insufficient funds.refunding the money.")
        return



def latte():
    cost = f.MENU['latte']['cost']
    quarter = 0.25 * int(input("How many quarters?"))
    dime = 0.1 * int(input("How many dimes?"))
    nickle = 0.05 * int(input("How many nickels?"))
    cents = 0.01 * int(input("How many cents?"))
    money_given = quarter + dime + nickle + cents

    if money_given > cost:
        f.resources['water'] = f.resources['water'] - 200
        f.resources['coffee'] = f.resources['coffee'] - 24
        f.resources['milk'] = f.resources['milk'] - 150
        return money_given - cost
    elif money_given == cost:
        f.resources['water'] = f.resources['water'] - 200
        f.resources['coffee'] = f.resources['coffee'] - 24
        f.resources['milk'] = f.resources['milk'] - 150
        return 0
    else:
        print("Insufficient funds.refunding the money.")
        return



def cappuccino():
    cost = f.MENU['cappuccino']['cost']
    quarter = 0.25 * int(input("How many quarters?"))
    dime = 0.1 * int(input("How many dimes?"))
    nickle = 0.05 * int(input("How many nickels?"))
    cents = 0.01 * int(input("How many cents?"))
    money_given = quarter + dime + nickle + cents

    if money_given > cost:
        f.resources['water'] = f.resources['water'] - 250
        f.resources['coffee'] = f.resources['coffee'] - 24
        f.resources['milk'] = f.resources['milk'] - 100
        return money_given - cost
    elif money_given == cost:
        f.resources['water'] = f.resources['water'] - 250
        f.resources['coffee'] = f.resources['coffee'] - 24
        f.resources['milk'] = f.resources['milk'] - 100
        return 0
    else:
        print("Insufficient funds.refunding the money.")
        return




machine_off = False
while machine_off==False:
    change=0.00
    choice = input("What would you like?(1.expresso\n2.cappuccino\n3.latte\n4.report\n5.off ")
    if choice == "expresso":
        if f.resources['water'] > 50 and f.resources['coffee'] > 18 :
            change = expresso()
            if change >0:
                print(f"Here is your change {change}.\n here is your expresso.")

            else:
                print("here is your expresso.")
        else:
            print("Insufficient resources.")
            machine_off=True


    elif choice == "cappuccino":
        if f.resources['water'] > 250 and f.resources['coffee'] > 24 and f.resources['milk'] > 100:
            change = cappuccino()
            if change > 0:
                print(f"Here is your change{change}.\n here is your cappuccino.")

            else:
                print("here is your cappuccino.")
        else:
            print("Insufficient resources.")
            machine_off = True


    elif choice == "latte":
        if f.resources['water'] > 200 and f.resources['coffee'] > 24 and f.resources['milk'] > 150:
            change = latte()
            if change >0:
                print(f"Here is your change{change}.\n here is you latte.")


            else:
                print("here is your latte.")
        else:
            print("Insufficient resources.")
            machine_off = True

    elif choice == "report":
        print(f.resources)
    else:
        machine_off = True
