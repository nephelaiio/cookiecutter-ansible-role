#!/usr/bin/env python

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
LICENSE_DIRECTORY = os.path.join(PROJECT_DIRECTORY, 'licenses')

if __name__ == '__main__':
    # configure selected license file and remove all other alternatives
    shutil.move(
            os.path.join(LICENSE_DIRECTORY, '{{ cookiecutter.license }}'),
            os.path.join(PROJECT_DIRECTORY, 'LICENSE'))
    shutil.rmtree(LICENSE_DIRECTORY)
