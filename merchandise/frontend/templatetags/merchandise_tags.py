from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def check_mark(value):
    """Returns a colored FontAwesome check mark or 'X' for a boolean value."""
    
    is_true = bool(value)

    if is_true:
        result = '<i class="fa fa-check text-success"></i>'
    else:
        result = '<i class="fa fa-times text-danger"></i>'
    
    return mark_safe(result)