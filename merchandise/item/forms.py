from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, Layout, ButtonHolder, Reset
from django.forms import Form, ModelForm, HiddenInput, CharField
from item.models import Item, ItemDetails


class ItemForm(ModelForm):
    """Item Create Form."""

    def __init__(self, *args, **kwargs):
        """Initialization method for form."""
        super(ItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.fields['details'].widget = HiddenInput()

    class Meta:
        model = Item
        fields = ['details', 'size', 'price', 'sku']

class ItemSearchForm(Form):
    """Item Search Form."""

    name = CharField(max_length=255, required=False, label="Name")

    def __init__(self, *args, **kwargs):
        super(ItemSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                'name'
            ), 
            ButtonHolder(
                Reset('Reset', 'reset')
            )
        )