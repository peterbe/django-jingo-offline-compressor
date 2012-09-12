from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import jingo
#from compressor.contrib.jinja2ext import CompressorExtension
from jingo_offline_compressor.jinja2ext import CompressorExtension
jingo.env.add_extension(CompressorExtension)

urlpatterns = patterns('',
    url(r'', include('project.otherapp.urls')),
    url(r'', include('project.myapp.urls')),
)

urlpatterns += staticfiles_urlpatterns()
