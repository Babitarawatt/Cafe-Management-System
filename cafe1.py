# Cafe Management System
# Sample Menu and Inventory
menu = {
    "Coffee": 5.0,
    "Tea": 3.0,
    "Sandwich": 7.0,
    "Cake": 4.5
}

inventory = {
    "Coffee": 50,
    "Tea": 50,
    "Sandwich": 20,
    "Cake": 30
}

sales = []

# Function to display menu
def display_menu():
    print("\n--- Leaf and Bean Cafe Menu ---")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    print()

# Function to take orders
def take_order():
    display_menu()
    order = {}
    print("Enter 'done' when finished ordering.")
    while True:
        item = input("Enter item name: ").title()
        if item.lower() == 'done':
            break
        if item not in menu:
            print("Item not on the menu.")
            continue
        quantity = int(input(f"Enter quantity of {item}: "))
        if inventory[item] < quantity:
            print(f"Sorry, only {inventory[item]} {item}(s) left in stock.")
            continue
        order[item] = quantity
    if order:
        process_order(order)

# Function to process an order
def process_order(order):
    total = 0
    print("\n--- Order Details ---")
    for item, qty in order.items():
        cost = menu[item] * qty
        total += cost
        inventory[item] -= qty
        print(f"{item} x{qty} = ${cost:.2f}")
    print(f"Total: ${total:.2f}")
    sales.append(total)
    print("Thank you for your order!\n")

# Function to view inventory
def view_inventory():
    print("\n--- Inventory ---")
    for item, stock in inventory.items():
        print(f"{item}: {stock} left")
    print()

# Function to view sales summary
def sales_summary():
    print("\n--- Sales Summary ---")
    print(f"Total Earnings: ${sum(sales):.2f}")
    print(f"Total Orders: {len(sales)}\n")

# Admin Menu
def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. View Menu")
        print("2. Add Menu Item")
        print("3. Remove Menu Item")
        print("4. View Inventory")
        print("5. View Sales Summary")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            display_menu()
        elif choice == '2':
            add_menu_item()
        elif choice == '3':
            remove_menu_item()
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            sales_summary()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

# Function to add menu items
def add_menu_item():
    item = input("Enter new item name: ").title()
    price = float(input(f"Enter price for {item}: "))
    stock = int(input(f"Enter initial stock for {item}: "))
    menu[item] = price
    inventory[item] = stock
    print(f"{item} added to the menu.\n")

# Function to remove menu items
def remove_menu_item():
    item = input("Enter item name to remove: ").title()
    if item in menu:
        del menu[item]
        del inventory[item]
        print(f"{item} removed from the menu.\n")
    else:
        print("Item not found on the menu.\n")

# Main Program
def main():
    while True:
        print("\n--- Welcome to Leaf and Bean Cafe ---")
        print("1. View Menu")
        print("2. Place Order")
        print("3. Admin Menu")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            display_menu()
        elif choice == '2':
            take_order()
        elif choice == '3':
            admin_menu()
        elif choice == '4':
            print("Thank you for visiting Leaf and Bean Cafe!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
