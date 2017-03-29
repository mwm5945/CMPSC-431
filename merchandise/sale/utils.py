from django.forms import model_to_dict
from item.models import Item
from sale.models import Sale
import locale

class Cart:
    """Represents a shopping cart."""
    
    def __init__(self, cart_items=dict()):
        self.cart_items = cart_items
    
    def get_total(self):
        total = 0
        for item in self.get_items():
            total += item['total']
        return total
    
    def get_total_display(self):
        locale.setlocale(locale.LC_ALL, '')
        return locale.currency(self.get_total())
    
    def get_items(self):
        locale.setlocale(locale.LC_ALL, '')
        items = Item.objects.filter(id__in=self.cart_items.keys())
        ret = []
        for i in items:
            temp = model_to_dict(i)
            temp['name'] = str(i)
            temp['quantity'] = self.cart_items[str(i.id)]
            temp['price'] = float(i.price)
            temp['price_display'] = locale.currency(temp['price'])
            temp['total'] = temp['price'] * temp['quantity']
            temp['total_display'] = locale.currency(temp['total'])
            ret.append(temp)
        return ret

    def add_item(self, item_id):
        item_id = str(item_id)
        if item_id in self.cart_items:
            self.cart_items[item_id] += 1
        else:
            self.cart_items[item_id] = 1
    