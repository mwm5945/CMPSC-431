from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Div, Layout, Submit

from django.forms import ModelForm

from . import models


class MerchInventoryAddItemForm(ModelForm):
    """Request form for adding an item to inventory."""

    def __init__(self, *args, **kwargs):
        """Initialization method for form."""
        super(MerchInventoryAddItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('item.item_name', css_class='col-md-6'),
                    Div('item.item_id', css_class='col-md-6'),
                    # PrependedText('item_price', '$'),
                    Div('item.item_description', css_class='col-md-12'),
                ),

            ),
            Div(
                ButtonHolder(
                    Submit('submit_request', 'Add Item', css_class='btn-primary'),
                ),
            )

        )

    class Meta:
        model = models.MerchandiseInventory

        exclude = ['item.thon_year_added', 'total_on_hand', 'item.item_price']

        labels = {
            'item.tem_name': 'Item Name:',
            'item.item_id': 'Item Barcode Number:',
            'item.item_description': 'Description of the Item (color, defining characteristics):',
            # 'item_price': 'Price of the item:', will be added later for POS system
            # 'item_amount1': 'Quantity in South Annex',
            # 'item_amount2': 'Quantity in Store A',
            # 'item_amount3': 'Quantity in Store C',
            # 'item_amount4': 'Quantity in Bravo Storage',
            # 'item_amount5': 'Quantity in Delta Storage',
        }
