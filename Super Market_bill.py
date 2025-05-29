import datetime

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name:15} | ${self.price:7.2f} | {self.quantity:3} | ${self.total_price():8.2f}"

class SupermarketBillingSystem:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        self.items.append(Item(name, price, quantity))
        print(f"Added {quantity} x {name} to cart.")

    def generate_bill(self):
        print("\n====== SUPER MARKET BILL ======")
        print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 40)
        print(f"{'Item':15} | {'Price':7} | Qty | {'Total':8}")
        print("-" * 40)

        subtotal = 0
        for item in self.items:
            print(item)
            subtotal += item.total_price()

        tax = subtotal * 0.10  # 10% tax
        total = subtotal + tax

        print("-" * 40)
        print(f"{'Subtotal':30} : ${subtotal:.2f}")
        print(f"{'Tax (10%)':30} : ${tax:.2f}")
        print(f"{'Total':30} : ${total:.2f}")
        print("================================")

    def reset_cart(self):
        self.items = []
        print("Cart cleared.")

def main():
    system = SupermarketBillingSystem()

    while True:
        print("\n--- Supermarket Billing System ---")
        print("1. Add Item")
        print("2. Generate Bill")
        print("3. Clear Cart")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter quantity: "))
                system.add_item(name, price, quantity)
            except ValueError:
                print("Invalid input. Price must be a number and quantity must be an integer.")
        elif choice == '2':
            system.generate_bill()
        elif choice == '3':
            system.reset_cart()
        elif choice == '4':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()