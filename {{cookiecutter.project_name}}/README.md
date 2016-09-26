{{ cookiecutter.galaxy_user }}.{{ cookiecutter.role_name }}
=========

[![Build Status](https://travis-ci.org/{{ cookiecutter.travis_user }}/{{ cookiecutter.project_name }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.travis_user }}/{{ cookiecutter.project_name }})

An [ansible role](https://galaxy.ansible.com/{{ cookiecutter.galaxy_user}}/{{ cookiecutter.role_name }}) to install and configure {{ cookiecutter.role_name }}

Requirements
------------

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](/requirements.txt)

Role Variables
--------------

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

Dependencies
------------

By default this role does not depend on any external roles. If any such dependency is required please [add them](/meta/main.yml) according to [the documentation](http://docs.ansible.com/ansible/playbooks_roles.html#role-dependencies)

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: {{ cookiecutter.role_name }} {{ cookiecutter.role_name }}_packages: {{ cookiecutter.role_name }} }


Testing
-------

Role is tested against the following distributions (docker images):
  * Ubuntu Xenial
  * CentOS 7
  * Debian Jessie
  * Arch Linux

You can test the role from sources using the command line using molecule directly
```
molecule test
```
Please review the [documentation](http://docs.ansible.com/ansible/galaxy.html#setup-travis-integrations) in order to add continuous integration for the role using [Travis CI](https://travis-ci.org). Role configuration is provided in the [Travis-CI configuration file](/travis.yml)

License
-------

This project is licensed under the terms of the [{{ cookiecutter.license }} License](/LICENSE)
