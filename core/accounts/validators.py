from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

"""
def validate_iranian_phone_number(value):
    if not value.startswith('09'):
        raise ValidationError(_('Phone number must start with 09.'))
    if len(value) != 11:
        raise ValidationError(_('Phone number must be exactly 11 characters long.'))
    if not value[2:].isdigit():
        raise ValidationError(_('Phone number must contain only numeric characters after 09.'))
"""


def validate_phone_number(value):
    pattern = r'^09\d{9}$'
    if not re.match(pattern, value):
        raise ValidationError('Enter a valid phone number')
    
    