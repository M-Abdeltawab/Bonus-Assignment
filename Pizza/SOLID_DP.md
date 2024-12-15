# SOLID Design Principles in the Pizza Ordering System  

## 1. Design Patterns Applied  

### Singleton Pattern  

- **Description**: The `InventoryManager` class utilizes the Singleton pattern to ensure that there is only one instance managing the inventory throughout the application.  
- **SOLID Principle**: Single Responsibility Principle (SRP) - The `InventoryManager` class handles all inventory-related functionality, maintaining a single responsibility.  

### Factory Method Pattern  

- **Description**: The `PizzaFactory` class creates `Pizza` instances (either `Margherita` or `Pepperoni`) based on user input, encapsulating the pizza creation logic.  
- **SOLID Principle**: Dependency Inversion Principle (DIP) - High-level modules (`main` function) do not depend on low-level modules (specific pizza types) but rather on abstractions (the `Pizza` interface).  

### Decorator Pattern  

- **Description**: Toppings are implemented using decorators (`CheeseDecorator`, `OlivesDecorator`, `MushroomsDecorator`), allowing dynamic additions to pizza objects.  
- **SOLID Principle**: Open/Closed Principle (OCP) - The pizza classes are open for extension (more toppings can be added) but closed for modification (existing classes do not need to change).  

### Strategy Pattern  

- **Description**: The payment method is structured using the Strategy pattern, with separate classes for `PayPal` and `CreditCard` that implement a common `PaymentStrategy` interface.  
- **SOLID Principle**: Interface Segregation Principle (ISP) - Payment strategies are separate interfaces that do not force clients to implement methods they do not use.  

## Conclusion  

By applying these design patterns, the pizza ordering system adheres to the SOLID principles, ensuring maintainability, scalability, and clarity in design.