# Write your code here
class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.state = "choosing an action"
    # Every time the user inputs a string to the console,
    # the program invokes this method with one argument: the line that user input to the console.

    #  store the current state of the machine
    #  the state could be "choosing an action" or "choosing a type of coffee"

    def get_input(self, input_):
        if self.state == "choosing an action":
            if input_ == "buy":
                self.state = "choosing a type of coffee"
            elif input_ == "fill":
                self.fill()
            elif input_ == "take":
                self.take()
            elif input_ == "remaining":
                self.print_state()
            elif input_ == "exit":
                exit()
        else:
            self.buy(input_)
            self.state = "choosing an action"

    def print_state(self):
        print("The coffee machine has:")
        print(self.water, " of water")
        print(self.milk, " of milk")
        print(self.beans, " of coffee beans")
        print(self.cups, " of disposable cups")
        print(self.money, " of money")

    def buy(self, coffee):
        espresso = [250, 16]  # water , beans
        latte = [350, 75, 20]  # water , milk , beans
        cappuccino = [200, 100, 12]  # water , milk , beans
        messages = ["Sorry, not enough water!", "Sorry, not enough milk!",
                    "Sorry, not enough beans!", "Sorry, not enough disposable cups!",
                    "I have enough resources, making you a coffee!"]

        if coffee != "back":
            if int(coffee) == 1:
                if self.water < espresso[0]:
                    print(messages[0])
                elif self.beans < espresso[1]:
                    print(messages[2])
                elif self.cups == 0:
                    print(messages[3])
                else:
                    print(messages[4])
                    self.water -= espresso[0]
                    self.beans -= espresso[1]
                    self.money += 4
                    self.cups -= 1
            elif int(coffee) == 2:
                if self.water < latte[0]:
                    print(messages[0])
                elif self.milk < latte[1]:
                    print(messages[1])
                elif self.beans < latte[2]:
                    print(messages[2])
                elif self.cups == 0:
                    print(messages[3])
                else:
                    print(messages[4])
                    self.water -= latte[0]
                    self.milk -= latte[1]
                    self.beans -= latte[2]
                    self.money += 7
                    self.cups -= 1
            elif int(coffee) == 3:
                if cappuccino[0] > self.water:
                    print(messages[0])
                elif cappuccino[1] > self.milk:
                    print(messages[1])
                elif cappuccino[2] > self.beans:
                    print(messages[2])
                elif self.cups == 0:
                    print(messages[3])
                else:
                    print(messages[4])
                    self.water -= cappuccino[0]
                    self.milk -= cappuccino[1]
                    self.beans -= cappuccino[2]
                    self.money += 6
                    self.cups -= 1
            else:
                print("Please choose the number between 1 and 3")

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input("> "))
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input("> "))
        print("Write how many grams of coffee beans do you want to add:")
        self.beans += int(input("> "))
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input("> "))

    def take(self):
        print("I gave you $", self.money)
        self.money = 0

#################################################################


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

while 1:
    if coffee_machine.state == "choosing an action":
        print("Write action (buy, fill, take, remaining, exit):")
        put = input()
        coffee_machine.get_input(put)
    else:
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        put = input("> ")
        coffee_machine.get_input(put)


