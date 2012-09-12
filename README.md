django-jingo-offline-compressor
===============================

(c) Peter Bengtsson, <mail@peterbe.com>, 2012
License: MIT

For elitists (e.g. me) who use
[jingo](https://github.com/jbalogh/jingo) to connect jinja2 with
Django a major drawback is that you can't do offline compression if
you use
[django_compressor](https://github.com/jezdez/django_compressor).     

The `compress` command that comes with `django_compressor` only works
for regular Django templates. :( 
Note though, that you can happily use `jingo` with `django_compressor`
but it only works its magic during runtime. This package aims to solve
that with a new command called `compress_jingo`.  

To install
----------

First install it by:

```
pip install django-jingo-offline-compressor
```

To start with, this assumes that you have `django_compressor` and
`jingo` set up and working. 

Add `jingo_offline_compressor` to your `INSTALLED_APPS`.

To run
------

Just like you'd run regular `django_compressor` you now run:

```
./manage.py compress_jingo
```

And remember, unless you have `COMPRESS_OFFLINE = True` in your
settings you might have to do: 

```
./manage.py compress_jingo --force
```

That should now have created all the minified and concatenated files
in your `STATIC_ROOT` in a sub-directory called `CACHE`.   

**Note:** If you have other apps in `INSTALLED_APPS` that have been
added to `JINGO_EXCLUDE_APPS` some of their templates might actually
be included in warnings when you run `compress_jingo`. Just ignore at
will.     

What's next
-----------

It's early days but hopefully if this stabilize and prove its
existence. Hopefully it can lead to a decent refactor and to have
tests so it can be patched upstream to `django_compressor`. Hint hint
@jezdez, keep an eye on me :)     


