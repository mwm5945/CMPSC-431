from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Div, HTML, Layout, Submit
from django.forms import ModelForm

from django.utils.translation import ugettext_lazy as _

from .models import Supplier


class SupplierSubmissionForm(ModelForm):
    """Form to add a new supplier."""

    def __init__(self, *args, **kwargs):
        """Initialization method for form."""

        super(SupplierSubmissionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'submit-once'
        self.helper.layout = Layout(
            Div(
                Div('name', css_class='col-md-6'),
                Div('phone', css_class='col-md-6'),
                css_class='row'
            ),
            HTML('<h4>Address</h4>'),
            'address__line_one',
            'address__line_two',
            Div(
                Div('address__city', css_class='col-md-3'),
                Div('address__state', css_class='col-md-3'),
                Div('address__zip', css_class='col-md-3'),
                css_class='row',
            ),
            'is_active',
            ButtonHolder(
                Submit('submit', 'Submit')
            )
        )

    class Meta:
        model = Supplier
        exclude = ['']
        labels = {
            'name': _('Company Name'),
            'phone': _('Phone Number'),
            'address__line_one': _('Line One'),
            'address__line_two': _('Line Two'),
            'address__city': _('City'),
            'address__state': _('State'),
            'address__zip': _('Zip'),
            'is_active': _('Is this an active supplier?')
        }
        help_texts = {
            'phone': _("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."),

        }