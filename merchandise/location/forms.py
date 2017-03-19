from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Div, Layout, Submit

from django.forms import ModelForm, DateField, DateInput, TextInput

from .models import Location


class CreateLocationForm(ModelForm):
    """Create Location Form."""

    def __init__(self, *args, **kwargs):
        """Initialization method for form"""
        super(CreateLocationForm, self).__init__(*args, **kwargs)
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
        # help_texts = {}
        # TODO: If we allow them to specify address when creating we need to think about format
        exclude = []
