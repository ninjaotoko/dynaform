# *-* coding:utf-8 *-*
import json
from django import forms
from dynaform.forms import widgets as custom_widgets
from django.core.validators import MaxValueValidator

max_value_validator = MaxValueValidator(0)

# Try importing ReCaptchaField
try:
    import ReCaptchaField
except ImportError:
    try:
        from captcha.fields import ReCaptchaField
    except ImportError:
        try: 
            from nocaptcha_recaptcha.fields \
                    import NoReCaptchaField as ReCaptchaField
        except ImportError:
            print 'ReCaptchaField was not loaded'


class CheckOtherField(forms.fields.MultiValueField):
    widget = custom_widgets.CheckOtherWidget
 
    def __init__(self, *args, **kwargs):
        list_fields = [forms.fields.BooleanField(required=False),
                       forms.fields.CharField()]
        super(CheckOtherField, self).__init__(list_fields, *args, **kwargs)
 
    def compress(self, values):
        return json.dumps(values)

class LinkbCaptchaField(forms.fields.CharField):
    default_validators = [max_value_validator]
