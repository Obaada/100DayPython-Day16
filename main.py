from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
available_menu = Menu()
coffee_maker = CoffeeMaker()
latte = MenuItem("latte", 200, 150, 24, 2.5)
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

running = True
while running:
    input_order = input(f"Welcome, what would you like to order? ({available_menu.get_items()}): ")
    if input_order == "off":
        print("Machine is turning off")
        running = False
    elif input_order == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        Drink = available_menu.find_drink(input_order)
        if coffee_maker.is_resource_sufficient(Drink):
            if money_machine.make_payment(Drink.cost):
                coffee_maker.make_coffee(Drink)





