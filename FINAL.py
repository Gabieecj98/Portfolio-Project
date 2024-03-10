Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:39) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Milestone 1
class ItemToPurchase:
    def __init__(self, item_name="none", item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

if __name__ == "__main__":
    print("Item")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers flavor:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
    print("\nItem 2")
    pepsi = ItemToPurchase()
    pepsi.item_name = input("Enter the pepsi flavor:\n")
    pepsi.item_price = float(input("Enter the pepsi price:\n"))
    pepsi.item_quantity = int(input("Enter the pepsi quantity:\n"))
    print("\nTOTAL COST")
    snickers.print_item_cost()
    pepsi.print_item_cost()
    total_cost = (snickers.item_quantity * snickers.item_price) + (pepsi.item_quantity * pepsi.item_price)
     print(f"\nTotal:${total_cost}")
     
SyntaxError: unexpected indent

class ItemToPurchase:
    def __init__(self, item_name="none", item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

            
if __name__ == "__main__":
    print("Item")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers flavor:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
    print("\nItem 2")
    pepsi = ItemToPurchase()
    pepsi.item_name = input("Enter the pepsi flavor:\n")
    pepsi.item_price = float(input("Enter the pepsi price:\n"))
    pepsi.item_quantity = int(input("Enter the pepsi quantity:\n"))
    print("\nTOTAL COST")
    snickers.print_item_cost()
    pepsi.print_item_cost()
    total_cost = (snickers.item_quantity * snickers.item_price) + (pepsi.item_quantity * pepsi.item_price)
    print(f"\nTotal:${total_cost}")

    
Item
Enter the snickers flavor:
Snickers Butterscotch
Enter the snickers price:
3:00
Traceback (most recent call last):
  File "<pyshell#26>", line 5, in <module>
    snickers.item_price = float(input("Enter the snickers price:\n"))
ValueError: could not convert string to float: '3:00'


class ItemToPurchase:
    def __init__(self, item_name="none", item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

        
if __name__ == "__main__":
    print("Item")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers flavor:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
    print("\nItem 2")
    pepsi = ItemToPurchase()
    pepsi.item_name = input("Enter the pepsi flavor:\n")
    pepsi.item_price = float(input("Enter the pepsi price:\n"))
    pepsi.item_quantity = int(input("Enter the pepsi quantity:\n"))
    print("\nTOTAL COST")
    snickers.print_item_cost()
    pepsi.print_item_cost()
    total_cost = (snickers.item_quantity * snickers.item_price) + (pepsi.item_quantity * pepsi.item_price)
    print(f"\nTotal:${total_cost}")

    
Item
Enter the snickers flavor:
Snickers Butterscotch
Enter the snickers price:
3.00
Enter the snickers quantity:
2

Item 2
Enter the pepsi flavor:
Cherry Pepsi
Enter the pepsi price:
1.89
Enter the pepsi quantity:
1

TOTAL COST
Traceback (most recent call last):
  File "<pyshell#32>", line 13, in <module>
    snickers.print_item_cost()
AttributeError: 'ItemToPurchase' object has no attribute 'print_item_cost'


class ItemToPurchase:
    def __init__(self, item_name="none", item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        
    def print_item_cost(self):
        
SyntaxError: unexpected indent

class ItemToPurchase:
    def __init__(self, item_name="none", item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

            
if __name__ == "__main__":
    print("Item")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers flavor:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
    print("\nItem 2")
    pepsi = ItemToPurchase()
    pepsi.item_name = input("Enter the pepsi flavor:\n")
    pepsi.item_price = float(input("Enter the pepsi price:\n"))
    pepsi.item_quantity = int(input("Enter the pepsi quantity:\n"))
    print("\nTOTAL COST")
    snickers.print_item_cost()
    pepsi.print_item_cost()
    total_cost = (snickers.item_quantity * snickers.item_price) + (pepsi.item_quantity * pepsi.item_price)
    print(f"\nTotal:${total_cost}")

    
Item
Enter the snickers flavor:
Snickers Butterscotch
Enter the snickers price:
3.00
Enter the snickers quantity:
2

Item 2
Enter the pepsi flavor:
Cherry Pepsi
Enter the pepsi price:
1.89
Enter the pepsi quantity:
1

TOTAL COST
Traceback (most recent call last):
  File "<pyshell#42>", line 13, in <module>
    snickers.print_item_cost()
AttributeError: 'ItemToPurchase' object has no attribute 'print_item_cost'


class ItemToPurchase:
    def __init__(self, item_name="none", item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

if __name__ == "__main__":
    print("Item")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers flavor:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
    print("\nItem 2")
...     pepsi = ItemToPurchase()
...     pepsi.item_name = input("Enter the pepsi flavor:\n")
...     pepsi.item_price = float(input("Enter the pepsi price:\n"))
...     pepsi.item_quantity = int(input("Enter the pepsi quantity:\n"))
...     print("\nTOTAL COST")
...     snickers.print_item_cost()
...     pepsi.print_item_cost()
...     total_cost = (snickers.item_quantity * snickers.item_price) + (pepsi.item_quantity * pepsi.item_price)
...     print(f"\nTotal: ${total_cost}")
... 
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> 
>>> 
>>> class ItemToPurchase:
...     def __init__(self, item_name="none", item_price="none", item_quantity=0):
...         self.item_name = item_name
...         self.item_price = item_price
...         self.item_quantity = item_quantity
... 
...     def print_item_cost(self):
...         print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")
... 
...         
>>> if __name__ == "__main__":
...     print("Item")
...     snickers = ItemToPurchase()
...     snickers.item_name = input("Enter the snickers flavor:\n")
...     snickers.item_price = float(input("Enter the snickers price:\n"))
...     snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
...     print("\nItem 2")
...     pepsi = ItemToPurchase()
...     pepsi.item_name = input("Enter the pepsi flavor:\n")
...     pepsi.item_price = float(input("Enter the pepsi price:\n"))
...     pepsi.item_quantity = int(input("Enter the pepsi quantity:\n"))
...     print("\nTOTAL COST")
...     snickers.print_item_cost()
...     pepsi.print_item_cost()
...     total_cost = (snickers.item_quantity * snickers.item_price) + (pepsi.item_quantity * pepsi.item_price)
...     print(f"\nTotal: ${total_cost}")
... 
...     
Item
Enter the snickers flavor:
Snickers Butterscotch
Enter the snickers price:
3.00
Enter the snickers quantity:
2

Item 2
Enter the pepsi flavor:
Cherry Pepsi
Enter the pepsi price:
1.89
Enter the pepsi quantity:
1

TOTAL COST
Snickers Butterscotch 2 @ $3.0 = $6.0
Cherry Pepsi 1 @ $1.89 = $1.89

Total: $7.89
