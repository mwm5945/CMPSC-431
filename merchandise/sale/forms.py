from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from item.models import Item
from django.forms.models import model_to_dict


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