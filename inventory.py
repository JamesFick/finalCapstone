from tabulate import tabulate


# ========The beginning of the class==========
class Shoe:

    # In this function, you must initialise the following attributes:
    #     ● country,
    #     ● code,
    #     ● product,
    #     ● cost, and
    #     ● quantity.
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        pass

    # Add the code to return the cost of the shoe in this method.
    def get_cost(self):
        return self.cost

    # Add the code to return the quantity of the shoes.
    def get_quantity(self):
        return self.quantity

    # Add a code to returns a string representation of a class.
    def __str__(self):
        return f'Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}'


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


# ==========Functions outside the class==============
# This function will open the file inventory.txt
# and read the data from this file, then create a shoes object with this data
# and append this object into the shoes list. One line in this file represents
# data to create one object of shoes. You must use the try-except in this function
# for error handling. Remember to skip the first line using your code.
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as inv:
            lines = inv.readlines()
            for i in range(1, len(lines)):
                line = lines[i].strip().split(',')
                shoe = Shoe(line[0], line[1], line[2], float(line[3]), int(line[4]))
                shoe_list.append(shoe)
    except Exception as error:
        print(f'Error: {error}. Try again!')


# This function will allow a user to capture data
# about a shoe and use this data to create a shoe object
# and append this object inside the shoe list.
def capture_shoes():
    country = input('Enter the origin country: ')
    code = input('Enter the code of a shoe: ')
    product = input('Enter the product name: ')
    cost = float(input('Enter the cost: '))
    quantity = int(input('Enter the quantity: '))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    with open("inventory.txt", "w") as file:
        for s in shoe_list:
            file.write(f"{s.country},{s.code},{s.product},{s.cost},{s.quantity}\n")


# This function will iterate over the shoes list and
# print the details of the shoes returned from the __str__
# function. Optional: you can organise your data in a table format
# by using Python’s tabulate module.
def view_all():
    print('\n***View all inventory***')
    view = input('\nWhich view would you like to display:\n'
                 '1 - Table view\n'
                 '2 - list view\n>>> ')
    if view == '1':
        temp = []
        for shoe in shoe_list:
            temp.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
        headers = ['Country', 'Code', 'Product', 'Cost', 'Quantity']
        print(tabulate(temp, headers, tablefmt="fancy_grid"))
    elif view == '2':
        for shoe in shoe_list:
            print(shoe.__str__())


# This function will find the shoe object with the lowest quantity,
# which is the shoes that need to be re-stocked. Ask the user if they
# want to add this quantity of shoes and then update it.
# This quantity should be updated on the file for this shoe.
def re_stock():
    print('\n***Restock inventory***')
    lowest_quantity = min(shoe.get_quantity() for shoe in shoe_list)
    for shoe in shoe_list:
        if shoe.get_quantity() == lowest_quantity:
            print(f'\nThe item with the lowest quantity is:\n{shoe.__str__()}')
            buy_more = input(f'\nWould you like to restock {shoe.product}?\nY/N >>> ')
            if buy_more.capitalize() == 'Y':
                quantity = int(input("Enter the quantity to restock: "))
                shoe.quantity += quantity
                print(f'\nThe new quantity for product: \'{shoe.product}\', is {shoe.quantity}.')
                with open("inventory.txt", "w") as file:
                    for s in shoe_list:
                        file.write(f"{s.country},{s.code},{s.product},{s.cost},{s.quantity}\n")
                    break
            elif buy_more.capitalize() == 'N':
                break
            else:
                print('Wrong input. Try again.')


#  This function will search for a shoe from the list
#  using the shoe code and return this object so that it will be printed.
def search_shoe():
    print('\n***Search***\n>>Enter \'X\' to go back to menu<<')
    while True:
        code = input('\nEnter the shoe code: ')
        if code.capitalize() == 'X':
            break
        for shoe in shoe_list:
            if shoe.code == code:
                print(shoe.__str__())
                break
            elif shoe == shoe_list[-1]:
                print('Wrong code, try again.')
                pass


# This function will calculate the total value for each item.
# Please keep the formula for value in mind: value = cost * quantity.
# Print this information on the console for all the shoes.
def value_per_item():
    i = 0
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        i += 1
        print(f'{i}. Product: \'{shoe.product}\'; total inventory value: {value}.')


# Write code to determine the product with the highest quantity and print this shoe as being for sale.
def highest_qty():
    print('\n***Highest quantity inventory***')
    highest_quantity = max(shoe.get_quantity() for shoe in shoe_list)
    for shoe in shoe_list:
        if shoe.get_quantity() == highest_quantity:
            print(f'\n{shoe.product} has the highest quantity: {shoe.quantity}.\n'
                  f'Product: \'{shoe.product}\'; Code: {shoe.code} is on sale now.')


# ==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
print("***MENU***")
read_shoes_data()
# print('but 0: ', shoe_list[0])
while True:
    choice = input("\nPlease enter:\n"
                   "1 - Add a new shoe to the system.\n"
                   "2 - View the inventory.\n"
                   "3 - Restock the minimum quantity item.\n"
                   "4 - Search for shoes.\n"
                   "5 - Total value for each item.\n"
                   "6 - The highest quantity product.\n"
                   "X - Exit\n>>> ")
    if choice == '1':
        capture_shoes()
    elif choice == '2':
        view_all()
    elif choice == '3':
        re_stock()
    elif choice == '4':
        search_shoe()
    elif choice == '5':
        value_per_item()
    elif choice == '6':
        highest_qty()
    elif choice.capitalize() == 'X':
        break
    else:
        print('\nWrong input. Try again.')
