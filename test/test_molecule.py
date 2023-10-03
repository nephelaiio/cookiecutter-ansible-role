import pytest
import os
import shutil
from subprocess import call
from cookiecutter.main import cookiecutter

test_commands = [
    "make lint",
    "make test"
]


@pytest.mark.parametrize('role_name', ['tree'])
def test_role_name(tmpdir, role_name):
    last_dir = os.path.curdir
    project_name = "nephelaiio.{0}".format(role_name)
    test_basename = project_name
    test_dir = os.path.join(tmpdir, test_basename)
    succeeds = lambda x: x == 0
    try:
        cookiecutter(
                '.',
                no_input=True,
                overwrite_if_exists=True,
                extra_context={'role_name': role_name}
        )
        shutil.move(test_basename, test_dir)
        os.chdir(test_dir)
        for command in test_commands:
            assert succeeds(call(command.split()))
    finally:
        os.chdir(last_dir)
        shutil.rmtree(test_dir, ignore_errors=True)
