from django.contrib.staticfiles.storage import staticfiles_storage

from jingo import register


@register.function
def static(path):
    r = staticfiles_storage.url(path)
    print repr(path), '--->', repr(r)
    return r
