from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Div, Layout, Submit

from django.forms import ModelForm, DateField, DateInput, TextInput

from . import models


class CreateScheduleForm(ModelForm):
    """Create Schedule Form."""


    def __init__(self, *args, **kwargs):
        """Initialization method for form"""
        super(CreateScheduleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'scheduled_employee',
            'location',
            Div('start_time', css_class='col-md-6'),
            Div('end_time', css_class='col-md-6'),

            ButtonHolder(
                Submit('submit', 'Submit'),
            )
        )

    class Meta:
        model = models.Shift
        help_texts = {
            'start_time': """Please enter in MM/DD/YYYY HH:MM 24-hour format""",
            'end_time': """Please enter in MM/DD/YYYY HH:MM 24-hour format""",
        }
        exclude = []
