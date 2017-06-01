# Example package with a console entry point
from __future__ import print_function
import os.path


def datafile(filename):
    from pkg_resources import resource_filename
    path = resource_filename("isu.autocomplete",
                             os.path.join('..', '..', '..', filename))
    path = os.path.abspath(path)
    return path
