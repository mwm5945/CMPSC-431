from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Layout, Submit

from django.forms import Form, ModelChoiceField, IntegerField

from location.models import Location

from item.models import Item
from .models import Inventory

class CreateInventoryTransactionForm(Form):
    """Create Schedule Form."""

    to_loc = ModelChoiceField(queryset=Location.objects.all())
    from_loc = ModelChoiceField(queryset=Location.objects.all())
    inventory = ModelChoiceField(queryset=Item.objects.all())
    quantity = IntegerField()

    def __init__(self, *args, **kwargs):
        """Initialization method for form"""
        super(CreateInventoryTransactionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'inventory',
            'quantity',
            'from_loc',
            'to_loc',
            ButtonHolder(
                Submit('submit', 'Submit'),
            )
        )
