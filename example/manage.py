#!/usr/bin/env python
import os
import sys
import warnings

if __name__ == "__main__":
    here = os.path.dirname(__file__)
    there = os.path.join(here, '..')
    there = os.path.abspath(there)
    sys.path.insert(0, there)
    print "NOTE Using jingo_offline_compressor from %s" % there

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
