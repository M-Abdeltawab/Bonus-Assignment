# Design Patterns Explained  

## 1. Singleton Pattern  

- **Explanation**: Ensures a class has only one instance and provides a global point of access to it. This is useful for scenarios where a shared resource needs to be managed, such as a configuration setting or a connection pool.  
- **Example**: The `InventoryManager` that manages pizza ingredients. It's crucial to keep a single inventory state across the program.  

## 2. Factory Method Pattern  

- **Explanation**: Defines an interface for creating an object but allows subclasses to alter the type of objects that will be created. It promotes loose coupling in code as the client code does not need to know about the concrete classes it needs to instantiate.  
- **Example**: The `PizzaFactory` class that generates different pizza types based on customer selection, allowing for easy extension without changing the client code.  

## 3. Decorator Pattern  

- **Explanation**: A structural pattern that allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class. It’s useful for adhering to the Open/Closed principle.  
- **Example**: The pizza toppings (`CheeseDecorator`, `OlivesDecorator`, and `MushroomsDecorator`) which dynamically add costs and descriptions to a pizza object.  

## 4. Strategy Pattern  

- **Explanation**: Defines a family of algorithms, encapsulates each one, and makes them interchangeable. It lets the algorithm vary independently from clients that use it, promoting flexibility and reusability.  
- **Example**: The varying payment methods (`PayPal` and `CreditCard`) that implement the `PaymentStrategy` interface.  

## 5. Overengineering Explained  

- **Overengineering** refers to implementing solutions that are more complex than necessary. This often happens when developers anticipate potential future needs that may never occur, leading to unnecessary complexity in codebase.  
  
- **Example of Overengineering**:   

  Suppose instead of managing inventory with a straightforward dictionary in Python, we decide to implement a complete relational database just to track pizza ingredients. This would involve setting up database connections, schema design, queries, ORM mappings, etc., which significantly complicates the system without significant benefit since inventory can be easily managed with a simple data structure in memory.  

```python  
# Overengineering Example: Inventory Using a Database Class  
class InventoryDatabase:  
    def __init__(self):  
        # Database connection and schema setup  
        print("Connecting to inventory database...")  

    def check_stock(self, item):  
        # Complex SQL query to check stock  
        pass  

    def update_stock(self, item):  
        # Complex SQL command to update stock  
        pass