# from abc import ABC, abstractmethod


# # Singleton Inventory Manager
# class InventoryManager:
#     _inventory = {
#         "Margherita": 10,
#         "Pepperoni": 10,
#         "Cheese": 15,
#         "Olives": 10,
#         "Mushrooms": 12,
#     }
#     def check_and_decrement(self, item: str) -> bool:
#         if self._inventory.get(item, 0) > 0:
#             self._inventory[item] -= 1
#             return True
#         return False

#     def get_inventory(self):
#         return self._inventory




# # Main Function
# def main():
#     inventory_manager = InventoryManager()

#     print("Welcome to the Pizza Restaurant!")


#     while True:

#         print("Choose your base pizza:")
#         print("1. Margherita ($5.0)")
#         print("2. Pepperoni ($6.0)")
#         print("0 => to exit")
#         pizza_choice = input("Enter the number of your choice: ")
#         if pizza_choice == '0':
#             break

#         # TODO: Fill the pizza creation. 
#         pizza = None
#         # Add toppings
#         while True:
#             print("\nAvailable toppings:")
#             print("1. Cheese ($1.0)")
#             print("2. Olives ($0.5)")
#             print("3. Mushrooms ($0.7)")
#             print("4. Finish order")
#             topping_choice = input("Enter the number of your choice: ")
#             # TODO: fill the following as required
#             # Cheese
#             if topping_choice == "1" :
#                 pass
#             # Olive
#             elif topping_choice == "2":
#                 pass
#             # Mushrooms
#             elif topping_choice == "3":
#                 pass
#             elif topping_choice == "4":
#                 break
#             else:
#                 print("Topping unavailable or out of stock!")

#         # Display final pizza details
#         print("\nYour order:")
#         print(f"Description: {pizza.get_description()}")
#         print(f"Total cost: ${pizza.get_cost():.2f}")

#         # Show final inventory
#         print("\nRemaining Inventory:")
#         print(inventory_manager.get_inventory())


# if __name__ == "__main__":
#     main()



from abc import ABC, abstractmethod  

# Singleton Inventory Manager  
class InventoryManager:  
    _instance = None  
    _inventory = {  
        "Margherita": 10,  
        "Pepperoni": 10,  
        "Cheese": 15,  
        "Olives": 10,  
        "Mushrooms": 12,  
    }  

    def __new__(cls):  
        if cls._instance is None:  
            cls._instance = super(InventoryManager, cls).__new__(cls)  
        return cls._instance  

    def check_and_decrement(self, item: str) -> bool:  
        if self._inventory.get(item, 0) > 0:  
            self._inventory[item] -= 1  
            return True  
        return False  

    def get_inventory(self):  
        return self._inventory  


class Pizza(ABC):  
    @abstractmethod  
    def get_description(self) -> str:  
        pass  

    @abstractmethod  
    def get_cost(self) -> float:  
        pass  


class Margherita(Pizza):  
    def get_description(self) -> str:  
        return "Margherita Pizza"  

    def get_cost(self) -> float:  
        return 5.0  


class Pepperoni(Pizza):  
    def get_description(self) -> str:  
        return "Pepperoni Pizza"  

    def get_cost(self) -> float:  
        return 6.0  


class PizzaFactory:  
    @staticmethod  
    def create_pizza(pizza_type: str) -> Pizza:  
        if pizza_type == "1":  
            return Margherita()  
        elif pizza_type == "2":  
            return Pepperoni()  
        else:  
            raise ValueError("Invalid Pizza Type")  


class PizzaDecorator(Pizza):  
    def __init__(self, pizza: Pizza):  
        self._pizza = pizza  

    def get_description(self) -> str:  
        return self._pizza.get_description()  

    def get_cost(self) -> float:  
        return self._pizza.get_cost()  


class CheeseDecorator(PizzaDecorator):  
    def get_description(self) -> str:  
        return self._pizza.get_description() + ", Cheese"  

    def get_cost(self) -> float:  
        return self._pizza.get_cost() + 1.0  


class OlivesDecorator(PizzaDecorator):  
    def get_description(self) -> str:  
        return self._pizza.get_description() + ", Olives"  

    def get_cost(self) -> float:  
        return self._pizza.get_cost() + 0.5  


class MushroomsDecorator(PizzaDecorator):  
    def get_description(self) -> str:  
        return self._pizza.get_description() + ", Mushrooms"  

    def get_cost(self) -> float:  
        return self._pizza.get_cost() + 0.7  


# Payment Strategy  
class PaymentStrategy(ABC):  
    @abstractmethod  
    def pay(self, amount: float) -> None:  
        pass  


class PayPal(PaymentStrategy):  
    def pay(self, amount: float) -> None:  
        print(f"Paying {amount:.2f} using PayPal.")  


class CreditCard(PaymentStrategy):  
    def pay(self, amount: float) -> None:  
        print(f"Paying {amount:.2f} using Credit Card.")  


# Main Function  
def main():  
    inventory_manager = InventoryManager()  
    print("Welcome to the Pizza Restaurant!")  

    while True:  
        print("Choose your base pizza:")  
        print("1. Margherita ($5.0)")  
        print("2. Pepperoni ($6.0)")  
        print("0 => to exit")  
        pizza_choice = input("Enter the number of your choice: ")  
        if pizza_choice == '0':  
            break  

        try:  
            pizza = PizzaFactory.create_pizza(pizza_choice)  
        except ValueError as e:  
            print(e)  
            continue  

        # Add toppings  
        while True:  
            print("\nAvailable toppings:")  
            print("1. Cheese ($1.0)")  
            print("2. Olives ($0.5)")  
            print("3. Mushrooms ($0.7)")  
            print("4. Finish order")  
            topping_choice = input("Enter the number of your choice: ")  

            if topping_choice == "1" and inventory_manager.check_and_decrement("Cheese"):  
                pizza = CheeseDecorator(pizza)  
            elif topping_choice == "2" and inventory_manager.check_and_decrement("Olives"):  
                pizza = OlivesDecorator(pizza)  
            elif topping_choice == "3" and inventory_manager.check_and_decrement("Mushrooms"):  
                pizza = MushroomsDecorator(pizza)  
            elif topping_choice == "4":  
                break  
            else:  
                print("Topping unavailable or out of stock!")  

        # Display final pizza details  
        print("\nYour order:")  
        print(f"Description: {pizza.get_description()}")  
        print(f"Total cost: ${pizza.get_cost():.2f}")  

        # Payment process  
        payment_method = input("Choose payment method (1: PayPal, 2: Credit Card): ")  
        if payment_method == "1":  
            payment_strategy = PayPal()  
        elif payment_method == "2":  
            payment_strategy = CreditCard()  
        else:  
            print("Invalid payment method!")  
            continue  

        payment_strategy.pay(pizza.get_cost())  

        # Show final inventory  
        print("\nRemaining Inventory:")  
        print(inventory_manager.get_inventory())  


if __name__ == "__main__":  
    main()