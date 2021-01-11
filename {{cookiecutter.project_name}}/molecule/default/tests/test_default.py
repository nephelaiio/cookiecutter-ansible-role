def test_command(host):
    assert host.command('{{ cookiecutter.role_name }} --version').rc == 0
