#!/usr/bin/env python
import sys
import os
import subprocess
from cookiecutter.main import cookiecutter

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("A role name must be provided")
    else: 
        role_name=sys.argv[1]
        project_name="ansible-role-{0}".format(role_name)
        cookiecutter(
                '.', 
                no_input=True, 
                overwrite_if_exists=True,
                extra_context={'role_name': role_name, 'project_name': project_name})
        os.chdir(project_name)
        test = subprocess.call(["molecule", "test"])
