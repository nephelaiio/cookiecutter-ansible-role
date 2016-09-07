#!/usr/bin/env python

import os
import shutil
from jinja2 import Environment, FileSystemLoader

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
LICENSE_DIRECTORY = os.path.join(PROJECT_DIRECTORY, 'licenses')
TEST_DIRECTORY = os.path.join(PROJECT_DIRECTORY, 'tests')
TEST_ROLE_DIRECTORY = os.path.join(TEST_DIRECTORY, 'roles')

if __name__ == '__main__':
    # configure selected license file and remove all other alternatives
    shutil.move(
            os.path.join(LICENSE_DIRECTORY, '{{ cookiecutter.license }}'),
            os.path.join(PROJECT_DIRECTORY, 'LICENSE'))
    shutil.rmtree(LICENSE_DIRECTORY)

    # configure self reference for role testing (see https://www.ansible.com/blog/testing-ansible-roles-with-docker)
    project_directory_relative = os.path.relpath(os.path.curdir, TEST_ROLE_DIRECTORY)
    project_directory_relative = os.path.join(project_directory_relative, os.path.pardir, '{{ cookiecutter.project_name }}')
    os.symlink(
            project_directory_relative,
            os.path.join(TEST_ROLE_DIRECTORY, '{{ cookiecutter.role_name }}'))

