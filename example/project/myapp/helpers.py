from django.contrib.staticfiles.storage import staticfiles_storage

from jingo import register


@register.function
def somefunction(input_):
    return input_.upper()
