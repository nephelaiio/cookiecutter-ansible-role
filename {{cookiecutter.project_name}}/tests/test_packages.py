from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = \
        AnsibleRunner('.molecule/ansible_inventory').get_hosts('test')


# see https://github.com/philpep/testinfra/issues/125
# @pytest.mark.parameterize('name', ['{{ cookiecutter.role_name }}'])
# def test_packages(Package, name):
#     assert Package(name).is_installed
def test_packages(Package):
    assert Package('{{ cookiecutter.role_name }}').is_installed
