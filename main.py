print("Welcome to the GC Fruit Market! ")
name = input('What is your name? ')
value = '0'
print(f'Welcome {name}. ')
price = 0
item1 = 0
item2 = 0
item3 = 0
item4 = 0
item5 = 0
item6 = 0
item_options = ["Apple $2", "Grape $1", "Orange $3"]
print("The item options are:")
print(f"1) {item_options[0]}")
print(f"2) {item_options[1]}")
print(f"3) {item_options[2]}")
item1 = input("Which Fruit would you like to buy? ")
if item1 == "1":
    print("You have purchased 1 apple at $2")
    price += 2
    add = input('Would you like to buy another peice of fruit? y/n ')
    if add == 'y':
        item_options = ["Apple $2", "Grape $1", "Orange $3"]
        print("The item options are:")
        print(f"1) {item_options[0]}")
        print(f"2) {item_options[1]}")
        print(f"3) {item_options[2]}")
        item2 = input("Which Fruit would you like to buy? ")
    elif add == 'n':
        tax = 0.05 * price
        totalprice = tax + price
        print(f'Your total is {price} with a 5% tax of {tax} coming to a grand total of {totalprice}')
if item1 == "2":
    print("You have purchased 1 Grape at $1")
    price += 1
    add = input('Would you like to buy another peice of fruit? y/n ')
    if add == 'y':
        item_options = ["Apple $2", "Grape $1", "Orange $3"]
        print("The item options are:")
        print(f"1) {item_options[0]}")
        print(f"2) {item_options[1]}")
        print(f"3) {item_options[2]}")
        item2 = input("Which Fruit would you like to buy? ")
    elif add == 'n':
        tax = 0.05 * price
        totalprice = tax + price
        print(f'Your total is {price} with a 5% tax of {tax} coming to a grand total of {totalprice}')
if item1 == "3":
    print("You have purchased 1 Orange at $3")
    price += 3
    add = input('Would you like to buy another peice of fruit? y/n ')
    if add == 'y':
        item_options = ["Apple $2", "Grape $1", "Orange $3"]
        print("The item options are:")
        print(f"1) {item_options[0]}")
        print(f"2) {item_options[1]}")
        print(f"3) {item_options[2]}")
        item2 = input("Which Fruit would you like to buy? ")
    elif add == 'n':
        tax = 0.05 * price
        totalprice = tax + price
        print(f'Your total is {price} with a 5% tax of {tax} coming to a grand total of {totalprice}')

if item2 == "1":
    print("You have purchased 1 apple at $2")
    price += 2
    add = input('Would you like to buy another peice of fruit? y/n ')
    if add == 'y':
        item_options = ["Apple $2", "Grape $1", "Orange $3"]
        print("The item options are:")
        print(f"1) {item_options[0]}")
        print(f"2) {item_options[1]}")
        print(f"3) {item_options[2]}")
        item3 = input("Which Fruit would you like to buy? ")
    elif add == 'n':
        tax = 0.05 * price
        totalprice = tax + price
        print(f'Your total is {price} with a 5% tax of {tax} coming to a grand total of {totalprice}')
if item2 == "2":
    print("You have purchased 1 Grape at $1")
    price += 1
    add = input('Would you like to buy another peice of fruit? y/n ')
    if add == 'y':
        item_options = ["Apple $2", "Grape $1", "Orange $3"]
        print("The item options are:")
        print(f"1) {item_options[0]}")
        print(f"2) {item_options[1]}")
        print(f"3) {item_options[2]}")
        item3 = input("Which Fruit would you like to buy? ")
    elif add == 'n':
        tax = 0.05 * price
        totalprice = tax + price
        print(f'Your total is {price} with a 5% tax of {tax} coming to a grand total of {totalprice}')
if item2 == "3":
    print("You have purchased 1 Orange at $3")
    price += 3
    add = input('Would you like to buy another peice of fruit? y/n ')
    if add == 'y':
        item_options = ["Apple $2", "Grape $1", "Orange $3"]
        print("The item options are:")
        print(f"1) {item_options[0]}")
        print(f"2) {item_options[1]}")
        print(f"3) {item_options[2]}")
        item3 = input("Which Fruit would you like to buy? ")
    elif add == 'n':
        tax = 0.05 * price
        totalprice = tax + price
        print(f'Your total is {price} with a 5% tax of {tax} coming to a grand total of {totalprice}')

if item3 == "1":
    print("You have purchased 1 apple at $2")
    price += 2
    add = input('Would you like to buy another peice of fruit? y/n ')
    if add == 'y':
        item_options = ["Apple $2", "Grape $1", "Orange $3"]
        print("The item options are:")
        print(f"1) {item_options[0]}")
        print(f"2) {item_options[1]}")
        print(f"3) {item_options[2]}")
        item4 = input("Which Fruit would you like to buy? ")
    elif add == 'n':
        tax = 0.05 * price
        totalprice = tax + price
        print(f'Your total is {price} with a 5% tax of {tax} coming to a grand total of {totalprice}')
if item3 == "2":
    print("You have purchased 1 Grape at $1")
    price += 1
    add = input('Would you like to buy another peice of fruit? y/n ')
    if add == 'y':
        item_options = ["Apple $2", "Grape $1", "Orange $3"]
        print("The item options are:")
        print(f"1) {item_options[0]}")
        print(f"2) {item_options[1]}")
        print(f"3) {item_options[2]}")
        item4 = input("Which Fruit would you like to buy? ")
    elif add == 'n':
        tax = 0.05 * price
        totalprice = tax + price
        print(f'Your total is {price} with a 5% tax of {tax} coming to a grand total of {totalprice}')
if item3 == "3":
    print("You have purchased 1 Orange at $3")
    price += 3
    add = input('Would you like to buy another peice of fruit? y/n ')
    if add == 'y':
        item_options = ["Apple $2", "Grape $1", "Orange $3"]
        print("The item options are:")
        print(f"1) {item_options[0]}")
        print(f"2) {item_options[1]}")
        print(f"3) {item_options[2]}")
        item4 = input("Which Fruit would you like to buy? ")
    elif add == 'n':
        tax = 0.05 * price
        totalprice = tax + price
        print(f'Your total is {price} with a 5% tax of {tax} coming to a grand total of {totalprice}')

if item4 == "1":
    print("You have purchased 1 apple at $2")
    price += 2
    add = input('Would you like to buy another peice of fruit? y/n ')
    if add == 'y':
        item_options = ["Apple $2", "Grape $1", "Orange $3"]
        print("The item options are:")
        print(f"1) {item_options[0]}")
        print(f"2) {item_options[1]}")
        print(f"3) {item_options[2]}")
        item5 = input("Which Fruit would you like to buy? ")
    elif add == 'n':
        tax = 0.05 * price
        totalprice = tax + price
        print(f'Your total is {price} with a 5% tax of {tax} coming to a grand total of {totalprice}')
if item4 == "2":
    print("You have purchased 1 Grape at $1")
    price += 1
    add = input('Would you like to buy another peice of fruit? y/n ')
    if add == 'y':
        item_options = ["Apple $2", "Grape $1", "Orange $3"]
        print("The item options are:")
        print(f"1) {item_options[0]}")
        print(f"2) {item_options[1]}")
        print(f"3) {item_options[2]}")
        item5 = input("Which Fruit would you like to buy? ")
    elif add == 'n':
        tax = 0.05 * price
        totalprice = tax + price
        print(f'Your total is {price} with a 5% tax of {tax} coming to a grand total of {totalprice}')
if item4 == "3":
    print("You have purchased 1 Orange at $3")
    price += 3
    add = input('Would you like to buy another peice of fruit? y/n ')
    if add == 'y':
        item_options = ["Apple $2", "Grape $1", "Orange $3"]
        print("The item options are:")
        print(f"1) {item_options[0]}")
        print(f"2) {item_options[1]}")
        print(f"3) {item_options[2]}")
        item5 = input("Which Fruit would you like to buy? ")
    elif add == 'n':
        tax = 0.05 * price
        totalprice = tax + price
        print(f'Your total is {price} with a 5% tax of {tax} coming to a grand total of {totalprice}')

if item5 == "1":
    print("You have purchased 1 apple at $2")
    price += 2
    add = input('Would you like to buy another peice of fruit? y/n ')
    if add == 'y':
        item_options = ["Apple $2", "Grape $1", "Orange $3"]
        print("The item options are:")
        print(f"1) {item_options[0]}")
        print(f"2) {item_options[1]}")
        print(f"3) {item_options[2]}")
        item6 = input("Which Fruit would you like to buy? ")
    elif add == 'n':
        tax = 0.05 * price
        totalprice = tax + price
        print(f'Your total is {price} with a 5% tax of {tax} coming to a grand total of {totalprice}')
if item5 == "2":
    print("You have purchased 1 Grape at $1")
    price += 1
    add = input('Would you like to buy another peice of fruit? y/n ')
    if add == 'y':
        item_options = ["Apple $2", "Grape $1", "Orange $3"]
        print("The item options are:")
        print(f"1) {item_options[0]}")
        print(f"2) {item_options[1]}")
        print(f"3) {item_options[2]}")
        item6 = input("Which Fruit would you like to buy? ")
    elif add == 'n':
        tax = 0.05 * price
        totalprice = tax + price
        print(f'Your total is {price} with a 5% tax of {tax} coming to a grand total of {totalprice}')
if item5 == "3":
    print("You have purchased 1 Orange at $3")
    price += 3
    add = input('Would you like to buy another peice of fruit? y/n ')
    if add == 'y':
        item_options = ["Apple $2", "Grape $1", "Orange $3"]
        print("The item options are:")
        print(f"1) {item_options[0]}")
        print(f"2) {item_options[1]}")
        print(f"3) {item_options[2]}")
        item6 = input("Which Fruit would you like to buy? ")
    elif add == 'n':
        tax = 0.05 * price
        totalprice = tax + price
        print(f'Your total is {price} with a 5% tax of {tax} coming to a grand total of {totalprice}')