import csv
from food_item import FoodItem

def save_to_file(filename, items):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Category", "Quantity", "Barcode", "Expiry Date"])
        for item in items:
            writer.writerow([item.name, item.category, item.quantity, item.barcode, item.expiry_date])

def load_from_file(filename):
    items = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            item = FoodItem(
                name=row["Name"],
                category=row["Category"],
                quantity=int(row["Quantity"]),
                barcode=row["Barcode"],
                expiry_date=row["Expiry Date"]
            )
            items.append(item)
    return items
