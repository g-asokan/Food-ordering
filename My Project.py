# This is an application that takes food orders

class Food:
    def __init__(self, name):
        self.name = name
        self.sold = []    # creates a new empty list

    def add_item(self, item):
        self.sold.append(item)


t = Food('Order')
a = 0

while a==0:

    print('Welcome to Habanero & Chips! the menu will be displayed below: ')

    print('1) Taco', '\n' , '2) Burrito' , '\n','3) Enchiladas' , '\n' , '4) Tostadas')

    Order = int(input('Select the respective number to place your order\n'))

    def CustomerOrder(selection):
        if selection == 1:
            return 'You got tacos!'

        if selection == 2:
            return 'You got burritos!'

        if selection == 3:
            return 'You got Enchiladas!'

        if selection == 4:
            return 'You got Tostadas!'


    print('Would you like to add any items?')

    Additional = input('Salsa, Chips, and/or Coke?\n')

    def AdditionalItems(selection):
        if selection == ('Salsa' or 'salsa'):
            t.add_item('Salsa')
            return(t.sold[0])
        if selection == ('Chips' or 'chips'):
            t.add_item('Chips')
            return(t.sold[0])
        if selection == ('Coke' or 'coke'):
            t.add_item('Coke')
            return(t.sold[0])
        else:
            return 'Item not in menu, try again!'

    print(CustomerOrder(Order), " with ", AdditionalItems(Additional))

    