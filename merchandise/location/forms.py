from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Div, Layout, Submit, HTML

from django.forms import ModelForm

from .models import Location
from directory.models import Address


class LocationForm(ModelForm):
    """Create Location Form."""

    def __init__(self, *args, **kwargs):
        """Initialization method for form"""
        super(LocationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'address',
            HTML("""<a href="{% url 'location:address_create' %}">Create New Address</a>"""),
            'is_active',
            ButtonHolder(
                Submit('submit', 'Submit'),
            )
        )

    class Meta:
        model = Location
        exclude = []


class AddressForm(ModelForm):
    """Create Address Form."""

    def __init__(self, *args, **kwargs):
        """Initialization method for form"""
        super(AddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'line_one',
            'line_two',
            'city',
            'state',
            'zip',
            ButtonHolder(
                Submit('submit', 'Submit'),
            )
        )

    class Meta:
        model = Address
        exclude = []