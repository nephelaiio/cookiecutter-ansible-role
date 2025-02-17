import os
import shutil
from subprocess import call

import pytest
from cookiecutter.main import cookiecutter

test_commands = ["make lint", "make test"]


# Helper function to check if a command succeeded
def succeeds(x):
    return x == 0


@pytest.mark.parametrize("role_name", ["tree"])
# Test whether the role_name is valid
def test_role_name(tmpdir, role_name):
    last_dir = os.path.curdir
    project_name = "nephelaiio.{0}".format(role_name)
    test_basename = project_name
    test_dir = os.path.join(tmpdir, test_basename)
    try:
        cookiecutter(
            ".",
            no_input=True,
            overwrite_if_exists=True,
            extra_context={"role_name": role_name},
        )
        shutil.move(test_basename, test_dir)
        os.chdir(test_dir)
        assert succeeds(call("devbox run make lint".split()))
        assert succeeds(call("devbox run make test".split()))
    finally:
        os.chdir(last_dir)
        shutil.rmtree(test_dir, ignore_errors=True)
