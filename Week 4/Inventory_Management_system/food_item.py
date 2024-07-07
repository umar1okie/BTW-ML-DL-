from datetime import datetime

class FoodItem:
    def __init__(self, name, category, quantity, barcode, expiry_date):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.barcode = barcode
        self.expiry_date = expiry_date

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}, Quantity: {self.quantity}, Barcode: {self.barcode}, Expiry Date: {self.expiry_date}"

    @classmethod
    def from_input(cls):
        name = input("Enter name: ")
        category = input("Enter category: ")
        quantity = int(input("Enter quantity: "))
        barcode = input("Enter barcode: ")
        expiry_date = datetime.strptime(input("Enter expiry date (YYYY-MM-DD): "), "%Y-%m-%d").date()
        return cls(name, category, quantity, barcode, expiry_date)
