from django import forms
from django.forms.models import model_to_dict

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, ButtonHolder

from directory.models import Customer
from location.models import Location
from item.models import Item
from sale.models import Transaction, Sale


class BarcodeForm(forms.Form):
    """Item Barcode Search Form."""

    barcode = forms.IntegerField(
        label = "Barcode",
        required = True,
        widget = forms.NumberInput(attrs={'autofocus': 'autofocus'}) 
    )

    def __init__(self, *args, **kwargs):
        """Initialization method for form."""
        super(BarcodeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    
    def clean_barcode(self):
        cleaned_data = self.cleaned_data

        if not Item.objects.filter(sku=cleaned_data['barcode']).exists():
            raise forms.ValidationError("No item found with barcode {}".format(cleaned_data['barcode']))
        else:
            item = Item.objects.get(sku=cleaned_data['barcode'])
            cleaned_data['item'] = item.id
        
        return cleaned_data


class TransactionForm(forms.Form):
    """Form for a new Transaction."""

    customer_email = forms.EmailField(
        label = "Customer Email"
    )
    transaction_type = forms.ChoiceField(choices=Transaction.TRANSACTION_TYPE_CHOICES)
    location = forms.ModelChoiceField( 
        label="Location",
        queryset=Location.objects.all(), 
        empty_label=None
    )

    def __init__(self, *args, **kwargs):
        """Initialization method for form."""
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    
    def clean_customer_email(self):
        cleaned_data = self.cleaned_data

        customer, created = Customer.objects.get_or_create(email=cleaned_data['customer_email'])
        cleaned_data['customer'] = customer

        return cleaned_data


class SaleReturnForm(forms.Form):
    """Form to return a sale."""

    sale = forms.ModelChoiceField(
        queryset=Sale.objects.all(), 
        empty_label=None
    )
    location = forms.ModelChoiceField( 
        label="Return Location",
        queryset=Location.objects.all(), 
        empty_label=None
    )

    def __init__(self, *args, **kwargs):
        super(SaleReturnForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                'location'
            ), 
            Field('sale', type="hidden"),
            ButtonHolder(
                Submit('Submit', 'submit')
            )
        )