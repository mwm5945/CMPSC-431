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


@register.filter
def five_stars(value):
    """Returns 0-5 filled in stars according to the input value."""

    filled_stars = int(value)
    non_filled_stars = 5 - filled_stars
    result = ''

    for s in range(0,filled_stars):
        result += '<i class="fa fa-star text-primary"></i>'

    for s in range(0,non_filled_stars):
        result += '<i class="fa fa-star-o text-primary"></i>'

    return mark_safe(result)

