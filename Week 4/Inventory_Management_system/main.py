from inventory import Inventory
from food_item import FoodItem
import file_manager
from datetime import datetime

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Food Item")
        print("2. Edit Food Item")
        print("3. Delete Food Item")
        print("4. Search Food Item")
        print("5. Get Near-Expiry Items")
        print("6. Save to File")
        print("7. Load from File")
        print("8. Generate Report")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            food_item = FoodItem.from_input()
            inventory.add_food_item(food_item)
            print("Food item added successfully.")

        elif choice == '2':
            barcode = input("Enter barcode of the item to edit: ")
            name = input("Enter new name (leave blank to keep current): ")
            category = input("Enter new category (leave blank to keep current): ")
            quantity = input("Enter new quantity (leave blank to keep current): ")
            expiry_date = input("Enter new expiry date (YYYY-MM-DD) (leave blank to keep current): ")
            kwargs = {}
            if name: kwargs['name'] = name
            if category: kwargs['category'] = category
            if quantity: kwargs['quantity'] = int(quantity)
            if expiry_date: kwargs['expiry_date'] = datetime.strptime(expiry_date, "%Y-%m-%d").date()
            print(inventory.edit_food_item(barcode, **kwargs))

        elif choice == '3':
            if not inventory.items:
                print("No food items to delete.")
            else:
                delete_by = input("Delete by (1) Barcode or (2) Name: ")
                if delete_by == '1':
                    barcode = input("Enter barcode of the item to delete: ")
                    if any(item.barcode == barcode for item in inventory.items):
                        print(inventory.delete_food_item(barcode))
                    else:
                        print("No such food item in the inventory.")
                elif delete_by == '2':
                    name = input("Enter name of the item to delete: ")
                    items_to_delete = [item for item in inventory.items if item.name == name]
                    if items_to_delete:
                        for item in items_to_delete:
                            inventory.delete_food_item(item.barcode)
                        print(f"Deleted {len(items_to_delete)} item(s) named {name}.")
                    else:
                        print("No such food item in the inventory.")
                else:
                    print("Invalid choice. Please try again.")

        elif choice == '4':
            name = input("Enter name to search (leave blank to skip): ")
            category = input("Enter category to search (leave blank to skip): ")
            barcode = input("Enter barcode to search (leave blank to skip): ")
            results = inventory.search_food_item(name=name, category=category, barcode=barcode)
            if results:
                for item in results:
                    print(item)
            else:
                print("No matching food items found.")

        elif choice == '5':
            days = int(input("Enter number of days to check for near-expiry items: "))
            near_expiry_items = inventory.get_near_expiry_items(days=days)
            if near_expiry_items:
                for item in near_expiry_items:
                    print(item)
            else:
                print("No near-expiry items found.")

        elif choice == '6':
            filename = input("Enter filename to save to: ")
            if not filename.endswith(".csv"):
                filename += ".csv"
            file_manager.save_to_file(filename, inventory.items)
            print(f"Inventory saved to {filename}.")

        elif choice == '7':
            filename = input("Enter filename to load from: ")
            if not filename.endswith(".csv"):
                filename += ".csv"
            inventory.items = file_manager.load_from_file(filename)
            print(f"Inventory loaded from {filename}.")

        elif choice == '8':
            print("\nReport Types")
            print("1. Near Expiry")
            print("2. Low Stock")
            print("3. Category Summary")
            report_choice = input("Enter your choice of report: ")
            if report_choice == '1':
                report = inventory.generate_report('near_expiry')
            elif report_choice == '2':
                report = inventory.generate_report('low_stock')
            elif report_choice == '3':
                report = inventory.generate_report('category_summary')
            else:
                report = "Invalid choice."
            print(report)

        elif choice == '9':
            print("Exiting the Inventory Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
