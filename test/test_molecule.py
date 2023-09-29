import pytest
import os
import shutil
from subprocess import call
from cookiecutter.main import cookiecutter


role_name = os.environ["ROLE_NAME"]
user_name = os.environ["USER_NAME"]
setup_commands = ['poetry install']
setup_success = 0
test_commands = ["poetry run molecule test"]
test_success = 0


@pytest.mark.parametrize('user', [user_name])
@pytest.mark.parametrize( 'role', [role_name])
def test_role(user, role):
    last_dir = os.path.curdir
    project_name = "nephelaiio.{0}".format(role)
    test_dir = project_name
    try:
        shutil.rmtree(test_dir, ignore_errors=True)
        cookiecutter(
                '.',
                no_input=True,
                overwrite_if_exists=True,
                extra_context={'role_name': role, 'galaxy_user': user}
        )
        for command in setup_commands:
            assert call(command.split()) == setup_success
        os.chdir(test_dir)
        for command in test_commands:
            assert call(command.split()) == test_success
    finally:
        os.chdir(last_dir)
        shutil.rmtree(test_dir, ignore_errors=True)
