from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Div, Layout, Submit

from django.forms import ModelForm

from .models import Location


class LocationForm(ModelForm):
    """Create Location Form."""

    def __init__(self, *args, **kwargs):
        """Initialization method for form"""
        super(LocationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'address',
            'is_active',
            ButtonHolder(
                Submit('submit', 'Submit'),
            )
        )

    class Meta:
        model = Location
        exclude = []
