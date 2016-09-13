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
        cookiecutter(
                '.', 
                no_input=True, 
                overwrite_if_exists=True,
                extra_context={'role_name': role_name, 'project_name': role_name})
        os.chdir(role_name)
        test = subprocess.call(["molecule", "test"])
