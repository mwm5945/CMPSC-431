from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Layout, Submit

from django.forms import Form, ModelChoiceField, IntegerField

from location.models import Location

from item.models import Item
from .models import Inventory

class UpdateInventoryForm(Form):
    """Create Schedule Form."""

    quantity = IntegerField()

    def __init__(self, *args, **kwargs):
        """Initialization method for form"""
        super(UpdateInventoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'quantity',
            ButtonHolder(
                Submit('submit', 'Submit'),
            )
        )


class CreateInventoryTransactionForm(Form):
    """Create Schedule Form."""

    to_location = ModelChoiceField(queryset=Location.objects.all())
    from_location = ModelChoiceField(queryset=Location.objects.all())
    item = ModelChoiceField(queryset=Item.objects.all())
    quantity = IntegerField()

    def __init__(self, *args, **kwargs):
        """Initialization method for form"""
        super(CreateInventoryTransactionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'item',
            'quantity',
            'from_location',
            'to_location',
            ButtonHolder(
                Submit('submit', 'Submit'),
            )
        )
