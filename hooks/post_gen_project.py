#!/usr/bin/env python

import os
import shutil
from jinja2 import Environment, FileSystemLoader

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
LICENSE_DIRECTORY = os.path.join(PROJECT_DIRECTORY, 'licenses')
TEST_DIRECTORY = os.path.join(PROJECT_DIRECTORY, 'tests')
TEST_ROLE_DIRECTORY = os.path.join(TEST_DIRECTORY, 'roles')
PROJECT_TEST_SYMLINK_PATH = os.path.join(TEST_ROLE_DIRECTORY, '{{ cookiecutter.role_name }}')

if __name__ == '__main__':
    # configure selected license file and remove all other alternatives
    shutil.move(
            os.path.join(LICENSE_DIRECTORY, '{{ cookiecutter.license }}'),
            os.path.join(PROJECT_DIRECTORY, 'LICENSE'))
    shutil.rmtree(LICENSE_DIRECTORY)

    # configure self reference for role testing (see https://www.ansible.com/blog/testing-ansible-roles-with-docker)
    project_test_symlink_target = \
            os.path.relpath(os.path.curdir, 
                    TEST_ROLE_DIRECTORY)
    project_test_symlink_target = \
            os.path.join(project_test_symlink_target, 
                    os.path.pardir, '{{ cookiecutter.project_name }}')
    if not os.path.exists(TEST_ROLE_DIRECTORY): 
        os.mkdir(TEST_ROLE_DIRECTORY)
    if not os.path.exists(PROJECT_TEST_SYMLINK_PATH): 
        os.symlink(project_test_symlink_target, PROJECT_TEST_SYMLINK_PATH)

