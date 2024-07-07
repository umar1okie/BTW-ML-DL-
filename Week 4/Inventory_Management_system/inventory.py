from datetime import datetime, timedelta
from food_item import FoodItem

class Inventory:
    def __init__(self):
        self.items = []

    def __iter__(self):
        return iter(self.items)

    def add_food_item(self, food_item):
        self.items.append(food_item)

    def edit_food_item(self, barcode, **kwargs):
        for item in self.items:
            if item.barcode == barcode:
                item.name = kwargs.get('name', item.name)
                item.category = kwargs.get('category', item.category)
                item.quantity = kwargs.get('quantity', item.quantity)
                item.expiry_date = kwargs.get('expiry_date', item.expiry_date)
                return "Food item edited successfully."
        return "Food item not found."

    def delete_food_item(self, barcode):
        if not self.items:
            return "No food items to delete."
        self.items = [item for item in self.items if item.barcode != barcode]
        return "Food item deleted successfully."

    def search_food_item(self, name=None, category=None, barcode=None):
        results = []
        for item in self.items:
            if (name and item.name == name) or (category and item.category == category) or (barcode and item.barcode == barcode):
                results.append(item)
        return results

    def get_near_expiry_items(self, days=7):
        near_expiry_items = []
        today = datetime.now().date()
        for item in self.items:
            if (item.expiry_date - today).days <= days:
                near_expiry_items.append(item)
        return near_expiry_items

    def near_expiry_generator(self, days=7):
        today = datetime.now().date()
        for item in self.items:
            if (item.expiry_date - today).days <= days:
                yield item

    def generate_report(self, report_type):
        if report_type == 'near_expiry':
            return self.get_near_expiry_items()
        elif report_type == 'low_stock':
            return [item for item in self.items if item.quantity < 5]
        elif report_type == 'category_summary':
            summary = {}
            for item in self.items:
                if item.category in summary:
                    summary[item.category] += 1
                else:
                    summary[item.category] = 1
            return summary
        else:
            return "Invalid report type."
